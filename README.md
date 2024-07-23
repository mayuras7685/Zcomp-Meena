# **[Zcomp](#Zcomp)**

The compiler which compiles, generates and verify proofs for different popular high-level language computations.
It's been used to compile **{ C , Rust , Python , Solidity , Zokrates }** to **{ R1CS }** , but its backend capability can expanded to many other cryptosystems like Fully Homomorphic Encryptions(FHE), Multi Party Computations , etc.

## **[Usage](#usage)**

> git clone https://github.com/mayuras7685/Zcomp-Meena
Then run this shell script in the Zcomp-Meena directory

> python3  api.py
Then you'll be prompted to input three types of files :

- source file ( supported types --> .sol , .py , .rs , .zok , .c)
- .pin file (contains the inputs required for proving) 
- .vin file (verifier inputs{can be thought as analogous to expected output})

After inputing these three files , the proof will be generated for these source files and verified simultaneously as well.


## **[Structure](#structure)**
```
└── circ

    ├── Cargo.lock
    ├── Cargo.toml
    ├── Dockerfile
    ├── LICENSE-APACHE
    ├── LICENSE-MIT
    ├── README.md
    ├── README_zsharp.md
    ├── circ_field
    ├── circ_opt
    ├── doc
    ├── driver.py
    ├── examples
    │   ├── ZoKrates
    │   │   ├── opt
    │   │   ├── pf
    │   │   └── spartan
    ├── scripts
    │   ├── build_r1cs_c_test.zsh
    │   ├── compiler_asymptotics.zsh
    │   ├── cp_test.zsh
    │   ├── dependencies_arch.sh
    │   ├── dependencies_macos_homebrew.sh
    │   ├── dependencies_ubuntu.sh
    │   ├── opa_bench.zsh
    │   ├── profile_sha.zsh
    │   ├── ram_test.zsh
    │   ├── spartan_zok_test.zsh
    │   ├── test_c_r1cs.zsh
    │   ├── zokrates_test.zsh
    │   └── zx_tests 
    │       └── wrong_output_with_args.zxf.out
    ├── src
    │   ├── front
    │   │   ├── mod.rs
    │   │   └── zsharp
    │   │       ├── TODO
    │   │       ├── interp.rs
    │   │       ├── mod.rs
    │   │       ├── parser.rs
    │   │       ├── term.rs
    │   │       ├── uglinesses
    │   │       └── zvisit
    │   ├── ir
    │   │   ├── mod.rs
    │   │   ├── opt
    │   │   ├── proof.rs
    │   │   └── term
    ├── target(backend)
    │   │   ├── mod.rs
    │   │   ├── r1cs
    │   │   │   ├── bellman.rs
    │   │   │   ├── mirage
    │   │   │   ├── mirage.rs
    │   │   │   ├── mod.rs
    │   │   │   ├── opt.rs
    │   │   │   ├── proof.rs
    │   │   │   ├── spartan.rs
    │   │   │   ├── trans.rs
    │   │   │   └── wit_comp.rs  
    ├── third_party
    │   ├── README.md
    │   ├── ZoKrates
    │   │   ├── LICENSE
    │   │   ├── zokrates_parser
    │   │   │   ├── Cargo.lock
    │   │   │   ├── Cargo.toml
    │   │   │   ├── README.md
    │   │   │   └── src
    │   │   ├── zokrates_pest_ast
    │   │   │   ├── Cargo.lock
    │   │   │   ├── Cargo.toml
    │   │   │   ├── README.md
    │   │   │   └── src
    │   │   └── zokrates_stdlib
    │   │       ├── Cargo.toml
    │   │       ├── build.rs
    │   │       ├── src
    │   │       ├── stdlib
    │   │       └── tests
    │   ├── bin
    │   │   └── ABY
    │   │       └── aby_interpreter
    │   ├── hycc
    │   │   ├── README.md
    │   │   ├── adapted_costs.json
    │   │   └── original_costs.json
    │   └── opa
    │       ├── README.md
    │       ├── adapted_costs.json
    │       └── original_costs.json
    └── util.py

```



### **[CIRCIFY](#circify)**

Circify is a compiler infrastructure which compiles high level language **{c , zokrates}** to **{R1CS , SMT , ILP}**. A high level overview of how the CirC infratructure works is as follows:

- First of all it converts high level language 
to **CIRC-IR**  using the compiler frontend which will be obtained in form of **EQC(Existentially Quantified Circuit)** .

* EQCs have two main features that differentiate them from CPUs, the targets of traditional compilers. First, EQCs are stateless—they do not support mutable variables, control flow, memory, or storage. Second, they admit non-determinism in the form of existentially quantified variables.

* After obtaining **CIRC-IR** we convert it into **R1CS** by following step:-

    - Optimizing IR
    * Lowering IR TO R1CS
    + Optimization of R1CS
    + Exporting our R1CS to bellman to convert into Groth16 , Marlin and the other proof systems supported by the rust crate



##  **[Z comp](#zcomp)**

Zcomp supports **{Rust , Solidity , python , C , Zokrates}** language as an input language for converting code into different cryptosystem.

## **[WORKFLOW](#workflow)**

### **[Frontend](#frontend)**

 - at the beginning we will give source code in these languages after going through frontend of compiler it will convert source code in AST(Abstract syntax tree).
 * then after recursively visiting all node of AST it will convert source code into CIRC-IR.
 + this CIRC-IR is obtained in the form of EQC(Existentially Quantified Circuit) which is a hard problem because it was converting source code into circuit.



### **[Backend](#backend)**

- after getting CIRC-IR we will do target-specific optimizations to our IR to make it convertible to R1CS (or any other constraint system for different proof generated algorithm)
* then we will lower our optimized CIRC-IR to R1CS

* after that we will optimize R1CS and export it into bellman and spartan to generate proof.
