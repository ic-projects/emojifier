package com.laurence;

import java.math.BigDecimal;
import java.util.ArrayList;

/**
 * Created by ljs116 on 24/01/17.
 */
public class TradePeriod {

    private final int timestamp;

    public ArrayList<Trade> trades = new ArrayList<>();
    public double high = -1;
    public double low = -1;
    public double open = -1;
    public double close = -1;
    public double vwap = 0;
    public int count = 0;
    public double totalAmount = 0;

    public TradePeriod(int timestamp) {
        this.timestamp = timestamp;
    }

    public void finalise(TradePeriod lastTrade) {
        if(count == 0) {
            high = lastTrade.high;
            low = lastTrade.low;
            open = lastTrade.open;
            close = lastTrade.close;
            vwap = lastTrade.vwap;
        } else {
            vwap = vwap / totalAmount;
        }
    }

    public void addTrade(Trade t) {
        trades.add(t);
        count++;
        if(open == -1) {
            open = t.getPrice();
        }
        close = t.getPrice();

        vwap += t.getPrice()*t.getAmount();
        totalAmount += t.getAmount();

        if(t.getPrice() > high || high == -1) {
            high = t.getPrice();
        }
        if(t.getPrice() < low || low == -1) {
            low = t.getPrice();
        }


    }

    public int getTimestamp() {
        return timestamp;
    }

    public String output() {
        String s = "";
        for(Trade t: trades) {
            //s = s + "["+ t.getPrice() + " , " + t.getAmount() + "]";
        }
        return "t:"+timestamp+" p:"+vwap+" h:"+high+" l:"+low+" c:"+close+" o:"+open+" a:"+totalAmount+" count:"+count + "   "+s;
    }
}
