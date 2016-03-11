from LCDGenerator import LCDGenerator


if __name__ == "__main__":
    gen = LCDGenerator('output', '#000000', '#00ff00')
    gen.generate_gif("u jelly motherfucker text")
    print("gif generated in 'results' folder")
    gen.clean_output_folder()