from stevedore.example import base


class MySimple(base.FormatterBase):
    """My basic formatter.
    """

    def format(self, data):
        """Format the data and return unicode text.

        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        """
        for name, value in sorted(data.items()):
            line = '{name} = {value} but it is mine\n'.format(
                name=name,
                value=value,
            )
            yield line
