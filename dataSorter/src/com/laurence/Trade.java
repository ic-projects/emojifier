package com.laurence;

/**
 * Created by ljs116 on 24/01/17.
 */
public class Trade {

    private final double amount;
    private final double price;

    public Trade(double amount, double price) {

        this.amount = amount;
        this.price = price;
    }

    public double getAmount() {
        return amount;
    }

    public double getPrice() {
        return price;
    }
}
