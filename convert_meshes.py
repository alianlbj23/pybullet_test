import os
import trimesh
import xml.etree.ElementTree as ET

def convert_stl_to_obj(mesh_dir):
    # 確保目錄存在
    if not os.path.exists(mesh_dir):
        print(f"錯誤: 找不到目錄 {mesh_dir}")
        return
    
    # 遍歷目錄中的所有 STL 文件
    for filename in os.listdir(mesh_dir):
        if filename.endswith('.stl'):
            stl_path = os.path.join(mesh_dir, filename)
            obj_path = os.path.join(mesh_dir, filename.replace('.stl', '.obj'))
            
            print(f"轉換: {filename} -> {filename.replace('.stl', '.obj')}")
            
            try:
                # 讀取 STL
                mesh = trimesh.load(stl_path)
                # 保存為 OBJ
                mesh.export(obj_path)
            except Exception as e:
                print(f"轉換 {filename} 時發生錯誤: {str(e)}")

def update_urdf_to_obj(urdf_path):
    # 註冊命名空間
    ET.register_namespace('', "http://www.ros.org/wiki/xacro")
    
    # 解析 URDF 文件
    tree = ET.parse(urdf_path)
    root = tree.getroot()
    
    # 修改所有 mesh 路徑從 .stl 到 .obj
    changes = 0
    for mesh in root.findall(".//*mesh"):
        if 'filename' in mesh.attrib:
            old_path = mesh.attrib['filename']
            if old_path.endswith('.stl'):
                new_path = old_path.replace('.stl', '.obj')
                mesh.attrib['filename'] = new_path
                changes += 1
                print(f"更新路徑: {old_path} -> {new_path}")
    
    # 保存修改後的文件
    tree.write(urdf_path, encoding='utf-8', xml_declaration=True)
    print(f"\n總共更新了 {changes} 個路徑")

if __name__ == "__main__":
    # 設置路徑
    mesh_dir = "excurate_arm/meshes"
    urdf_path = "excurate_arm/target.urdf"
    
    # 檢查並創建備份
    if not os.path.exists(urdf_path + ".backup"):
        import shutil
        shutil.copy2(urdf_path, urdf_path + ".backup")
        print(f"創建備份文件: {urdf_path}.backup") 