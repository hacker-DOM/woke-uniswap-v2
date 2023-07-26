# Dependencies

* [woke](https://github.com/Ackee-Blockchain/woke)
    * (in an isolated virtual environment, and with console scripts
    (executables) being accessible globally) `> pipx install woke`
    * in a separate virtual environment: `> pip install woke`
* [just](https://www.github.com/casey/just)

# Execution

* `> woke init pytype -w`: Starts pytypes in watch mode
* `> just fuzz`: Run fuzz tests
