project('c_quoted', 'c', meson_version: '>= 1.8')

c_quoted = executable(
  'c_quoted',
  'c_quoted.c',
  c_args: [
    '-DC_QUOTED_STR=' + get_option('unquoted_value').to_c_quoted(),
  ],
)

python = import('python').find_installation('python3')

test('test_c_quoted_str',
  python,
  args: [
    meson.current_source_dir() / 'test.py',
    c_quoted,
    get_option('unquoted_value'),
  ],
)

summary({
  'unquoted_value': get_option('unquoted_value'),
  'quoted_value': get_option('unquoted_value').to_c_quoted(),
})
