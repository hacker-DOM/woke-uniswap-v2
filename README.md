# Dependencies

* [woke](https://github.com/Ackee-Blockchain/woke) - the best development framework for Solidity
    * (in an isolated virtual environment, and with console scripts
    (executables) being accessible globally) `> pipx install woke`
    * in a separate virtual environment: `> pip install woke`
* [just](https://www.github.com/casey/just) - Just a command runner
    * `> brew install just`

# Execution

* `> woke init pytype -w`: Starts pytypes in watch mode
* `> just fuzz`: Run fuzz tests
