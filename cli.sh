#!/bin/bash
task() {

zok_file=$(basename "$1")
pin_file=$(basename "$2")
vin_file=$(basename "$3")

# Use the base names in your script
echo "ZoKrates file: $zok_file"
echo "Public input file: $pin_file"
echo "expected output file: $vin_file"
    cp "$zok_file" "/home/rajasree/circ/examples/ZoKrates/pf"
    echo "copied 1"
    cp "$pin_file" "/home/rajasree/circ/examples/ZoKrates/pf"
    echo "copied 2"
    cp "$vin_file" "/home/rajasree/circ/examples/ZoKrates/pf"
    echo "copied 3"
    echo "pf_test ${zok_file%.*}" >> scripts/zokrates_test.zsh
}

task "$1" "$2" "$3"
