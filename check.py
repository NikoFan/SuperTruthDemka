def text(text):
    return len(text) != 0


def numbers(number):
    try:
        return float(number) > 0
    except Exception as e:
        print(e, 1)
        return False


def main(data: dict):
    if (text(data['material_name']) and
            numbers(data['material_cost']) and
            numbers(data['material_paket_count']) and
            numbers(data['material_count']) and
            numbers(data['material_min_count']) and
            text(data['material_edinica'])
    ):
        return True
    return False
