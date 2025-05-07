#!/bin/bash
awk '/^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$/' file.txt
#calls awk, the pattern of the regex its tested each line
#compares the first possible pattern or the second 