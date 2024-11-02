import xml.etree.ElementTree as ET
import os

def fix_urdf_paths(urdf_path):
    # 註冊命名空間
    ET.register_namespace('', "http://www.ros.org/wiki/xacro")
    
    # 解析 URDF 文件
    tree = ET.parse(urdf_path)
    root = tree.getroot()
    
    # 計數器
    changes = 0
    
    # 打印當前所有的 mesh 路徑
    print("當前的 mesh 路徑:")
    for mesh in root.findall(".//*mesh"):
        if 'filename' in mesh.attrib:
            print(mesh.attrib['filename'])
    
    # 尋找所有的 mesh 元素（使用更廣泛的搜索）
    for mesh in root.findall(".//*mesh"):
        if 'filename' in mesh.attrib:
            old_path = mesh.attrib['filename']
            # 如果路徑包含 package://
            if 'package://' in old_path:
                # 提取文件名
                filename = old_path.split('/')[-1]
                # 建立新路徑
                new_path = f"meshes/{filename}"
                # 更新路徑
                mesh.attrib['filename'] = new_path
                changes += 1
                print(f"修改路徑: {old_path} -> {new_path}")
    
    # 保存修改後的文件
    tree.write(urdf_path, encoding='utf-8', xml_declaration=True)
    print(f"\n總共修改了 {changes} 個路徑")
    
    # 提醒用戶確保 meshes 目錄存在
    meshes_dir = os.path.join(os.path.dirname(urdf_path), 'meshes')
    if not os.path.exists(meshes_dir):
        print(f"\n注意: 請確保創建了 meshes 目錄: {meshes_dir}")

if __name__ == "__main__":
    urdf_path = "excurate_arm/target.urdf"
    
    # 檢查文件是否存在
    if not os.path.exists(urdf_path):
        print(f"錯誤: 找不到文件 {urdf_path}")
        exit(1)
    
    # 創建備份
    backup_path = urdf_path + ".backup"
    if not os.path.exists(backup_path):
        import shutil
        shutil.copy2(urdf_path, backup_path)
        print(f"創建備份文件: {backup_path}")
    
    # 修改 URDF
    fix_urdf_paths(urdf_path)