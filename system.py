import logging
import pickle



class System:

    def __init__(self):
        self.selected_investor = None

    def save_investor(self, inv):
        # to do: catch FileNotFoundError
        path_and_file = "Data/investor " + inv.name + ".json"
        with open(path_and_file, "wb") as outfile:
            pickle.dump(inv, outfile)
        msg = "Investor '" + inv.name + "' was saved in JSON-file."
        logging.info(msg)


    def load_investor(self, inv_name):
        path_and_file = "Data/investor " + inv_name + ".json"
        try:
            with open(path_and_file, "rb") as file:
                inv = pickle.load(file)
            logging.info("Investor " + inv_name + " loaded from file.")
        except FileNotFoundError:
            raise FileNotFoundError
        except Exception:
            raise

        return inv


if __name__ == '__main__':
    system = System()
    inv = system.load_investor(inv_name="Pet Peso")

    print(inv.first_name)
    print(inv.last_name)