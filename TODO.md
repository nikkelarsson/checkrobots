# TODO
- Add logging functionality. This would mainly be so that there would be better
  debugging abilities – as right now there is not!
- [x] Implement a functionality, that would make it possible to fetch the 'disallowed'
  endpoint fields only.
- [x] Implement a flag that would enable fetching both 'allowed' and 'disallowed'
  endpoint fields.
- Implement "-h" and "--help" flags.
- [x] In module "endpoints.py":
  - Create functions "count_allowed" and "count_disallowed".
- In module "headers.py":
  - Create a function "print_".
- [ ] Implement flag/flags that would enable fetching the contents of the
  robots.txt as is, in other words, as "raw".
- [ ] Create new branch, and in that branch do the following:
  - Move the "print_invalid_args" function to the "parsing.py" module.
- [ ] Delete the "print_headers" function from "main.py", as it is no longer
  needed there.
