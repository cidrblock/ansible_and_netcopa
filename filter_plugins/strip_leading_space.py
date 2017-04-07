def strip_leading_space(netcopa_filter_output):
    for entry in netcopa_filter_output:
        entry['lines'] = [x.lstrip() for x in entry['lines']]
    return netcopa_filter_output

class FilterModule(object):
    def filters(self):
        return {
            'strip_leading_space': strip_leading_space,
        }
