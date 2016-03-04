from LCDGenerator import LCDGenerator


if __name__ == "__main__":
    gen = LCDGenerator('output', '#000000', '#550012')
    gen.generate_gif("coucou")
    print("gif generated in result folder")
    gen.clean_output_folder()