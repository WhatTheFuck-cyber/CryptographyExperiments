from utils import *

if __name__ == "__main__":
    crypted_text = "ZITTDWSTDGYLXFNQZLTFXFOCTKLOZNOLEOKEXSQKOFLIQHTZITXHHTKHQKZYTQZXKTLZITYXSSGYYOEOQSEIOFTLTFQDTGYZITXFOCTKLOZNQKKQFUTRYKGDSTYZZGKOUIZQSGFUZITTRUTQFRZITSGVTKHQKZYTQZXKTLZITYXSSGYYOEOQSTFUSOLIFQDTQSLGQKKQFUTRYKGDSTYZZGKOUIZZITETFZTKROLHSQNLQEKQWQHHSTLIQHTRSQZZOETVOFRGVHQZZTKFZIOLHQZZTKFZQATLZITOEGFOEWXOSROFUUKQFRWTSSZGVTKGYZITYGKDTKFQZOGFQSUXQFURGFUXFOCTKLOZNQLZITDQOFRTLOUFTSTDTFZEGDWOFOFUZITQKZOLZOEEGFETHZOGFGYEIOFTLTUQKRTFLVOZIDGRTKFRTLOUFZTEIFOJXTLZITTDWSTDXLTLZITEKQWQHHSTLIQHTRSQZZOETVOFRGVQFRZITZGVTKOLQHHTQKQFETZGYGKDZITEIQKQEZTKLYGKLXFNQZZITZKTTLGFWGZILORTLGYZITVOFRGVRTEKTQLTOFLOMTYKGDYKGFZZGWQEAEKTQZOFUQLTFLTGYRTHZIQFRLHQZOQSSQNTKOFUZITEXKCTRLIQHTOFZITDORRSTESTCTKSNYGKDLQKTRAQHGAYSGVTKLNDWGSOMOFUZITXFOCTKLOZNOLSGEQZOGFOFZITSOFUFQFKTUOGFQETFZKQSQCTFXTYGKDTRWNZITYGXFROFUNTQKTDWGROTLZITHKGYGXFRQEQRTDOEYGXFRQZOGFQFRUSGKOGXLIOLZGKNGYLXFNQZLTFXFOCTKLOZNZITTDWSTDOLXLXQSSNKTFRTKTROFLZQFRQKRUKTTFKTHKTLTFZOFUSOYTUKGVZIQFRTZTKFOZNLNDWGSOMOFUZITCOZQSOZNQFRCOUGKGYZITXFOCTKLOZN"
    crypted_text.upper()
    sorted_letters = count_and_sort_letters(crypted_text)

    std_sorted_letters = "etaoinshrdlcumwfgypbvkjxqz"   # 标准频率分布
    if len(std_sorted_letters) != 26:
        print("频率分布表长不等于26！")
        exit(1)

    try_to_decrypt_text = decrypt_by_frequency(crypted_text, sorted_letters, std_sorted_letters)

    print("----------这是一个可能的解密，如果解密不对，请更换频率表----------")
    print(try_to_decrypt_text)

    print("----------保存这个解密----------")
    save_as_json(crypted_text, try_to_decrypt_text, std_sorted_letters)
