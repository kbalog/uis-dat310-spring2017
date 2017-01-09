/* BankAccount class */

function BankAccount(name, balance) {
    this.name = name;
    this.balance = balance;
    this.deposit = deposit;
    this.withdraw = withdraw;
    this.log = []; // equivalent to saying new Array();
    this.printLog = printLog;
}

function deposit(amount) {
    var oldBalance = this.balance;
    this.balance += amount;

    // log transaction
    this.log.push({
        transaction: "deposit",
        amount: amount,
        date: new Date(),
        oldBalance: oldBalance,
        newBalance: this.balance
    });
}

function withdraw(amount) {
    var oldBalance = this.balance;
    if (this.balance >= amount) {
        this.balance -= amount;
    }
    else {
        console.log("Error: insufficient funds!");
    }

    // log transaction
    this.log.push({
        transaction: "withdraw",
        amount: amount,
        date: new Date(),
        oldBalance: oldBalance,
        newBalance: this.balance
    });

}

function printLog() {
    for (var i = 0; i < this.log.length; i++) {
        console.log(this.log[i].date
        + "\t" + this.log[i].transaction
        + "\t" + this.log[i].amount
        + "\t" + this.log[i].oldBalance
        + "\t" + this.log[i].newBalance);
    }
}