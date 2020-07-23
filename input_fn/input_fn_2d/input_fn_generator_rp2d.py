import tensorflow as tf

import input_fn.input_fn_2d.data_gen_2dt.util_2d.interface as interface
from input_fn.input_fn_2d import input_fn_generator_2d


class InputFnRegularPolygon2D(input_fn_generator_2d):
    """Input Function Generator for regular polygon 2d problems, dataset returns a dict..."""

    def __init__(self, flags_):
        super(InputFnRegularPolygon2D, self).__init__(flags_)
        self.iterator = None
        self._next_batch = None
        self.dataset = None
        self._interface_obj = interface.InterfaceRegularPolygon2D(max_edges=self._flags.max_edges)


if __name__ == "__main__":
    print("run input_fn_generator_regular_polygon debugging...")
    import util.flags as flags
    import trainer.trainer_base  # do not remove, needed for flag imports


    # gen = Generator2dt(flags.FLAGS)
    # for i in range(10):
    #     in_data, tgt = gen.get_data().__next__()
    #     print("output", type(tgt["points"]), in_data["fc"].shape)
    #     # print(tgt["points"])
    #
    # print(os.getcwd())
    # flags.print_flags()
    #
    # input_fn = InputFnTriangle2D(flags.FLAGS)
    # train_dataset = input_fn.get_input_fn_train()
    # counter = 0
    # for i in train_dataset:
    #     counter += 1
    #     if counter >= 10:
    #         break
    #     in_data, tgt = i
    #     print("output", type(tgt["points"]), in_data["fc"].shape)
    #     # print(tgt["points"])
    #
    # print("Done.")
