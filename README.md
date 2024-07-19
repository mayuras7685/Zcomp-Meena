# **[Zcomp](#Zcomp)**

The compiler which compiles, generates and verify proofs for different popular high-level language computations.
It's been used to compile **{ C , Rust , Python , Solidity , Zokrates }** to **{ R1CS }** , but it probably also applies to any statically type high-level language.


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


## **[WORKFLOW](#workflow)**


## **[CIRCIFY](#circify)**

Circify is a compiler infrastructure which compiles high level language **{c , zokrates}** to **{R1CS , SMT , ILP}**.

- First of all it was converting high level language 
to **CIRC-IR**  using frontend which will be obtained in form of **EQC(Existentially Qualified Circuit)** .
* After obtaining **CIRC-IR** we convert it into **R1CS** by following step:-
    
    - Optimizing IR
    * Lowering IR TO R1CS
    + Optimization of R1Cs

    + Exporting our R1CS to bellman

##  **[Z comp](#zcomp)**

Z comp support **{Rust , Solidity , python , C , Zokrates}** language.

### **[Frontend](#frontend)**
 
 - at the beginning we will give source code in these languages after going through frontend of compiler it will convert source code in AST(Abstract syntax tree).
 * then after recursively visiting all node of AST it will convert source code into CIRC-IR.
 + this CIRC-IR is obtained in the form of EQC(Existentially Qualified Circuit) which is a hard problem because it was converting source code into circuit.



### **[Backend](#backend)**

- after getting CIRC-IR we will do target-specific optimizations to our IR to make it convertible to R1CS
* then we will lower our optimized CIRC-IR to R1CS

* after that we will optimize R1CS and export it into bellman and spartan to generate proof.

+  after converting it into Groth16 ,we will prove our circuit with the help of source code , .vin file and .pin file.
 
