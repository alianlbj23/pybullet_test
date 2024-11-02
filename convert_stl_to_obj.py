import os
import numpy as np
from stl import mesh
import trimesh

def convert_stl_to_obj(stl_path, obj_path):
    # 讀取STL
    mesh_data = trimesh.load(stl_path)
    # 保存為OBJ
    mesh_data.export(obj_path)

# 轉換目錄下所有STL文件
mesh_dir = "excurate_arm/meshes"
for file in os.listdir(mesh_dir):
    if file.endswith(".stl"):
        stl_path = os.path.join(mesh_dir, file)
        obj_path = os.path.join(mesh_dir, file.replace(".stl", ".obj"))
        print(f"Converting {stl_path} to {obj_path}")
        convert_stl_to_obj(stl_path, obj_path) 