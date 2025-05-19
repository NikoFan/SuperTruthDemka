class Material:
    material_name: str = None

    @staticmethod
    def set_material(new_mat): Material.material_name = new_mat

    @staticmethod
    def get_material() -> str: return Material.material_name