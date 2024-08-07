import atolibrary as ato

n = ato.lotto.get_one_number()
print("ato lotto number:", n)
print(ato.lotto.get_one_set())
print(ato.lotto.get_one_set_sorted())
print(ato.lotto.get_one_set_string())
print(ato.lotto.get_one_set_string_bracket())
print(ato.lotto.get_some_sets())
print(ato.lotto.get_some_sets(7))


name = ato.names.get_human_name()
print("ato name:", name)
print(ato.names.get_social_security_number())
print(ato.names.get_school_name())
print(ato.names.get_country_name())


print(ato.names.get_robot_name())
print(ato.names.get_vehicle_company())
print(ato.names.get_color_name())
print(ato.names.get_colors())