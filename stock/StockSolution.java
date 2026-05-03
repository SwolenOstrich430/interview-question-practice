class StockSolution1 {
    public int maxProfit(int[] prices) {
        if (prices.length == 0 || prices.length == 1) {
            return 0;
        } 
        /*
            buy only one share of stock at a time 
            you can only hold one share of stock at a time 
            but you can buy and sell stock on the same day
            want to find the biggest difference (small to low) between indices 
            and then also you're covering width of time where stock is held 
        */

        int idx = 1;
        int totalEarnings = 0;
        int buyPrice = -1;
        int leadPrice = prices[idx];
        int lagPrice = prices[idx - 1];

        while (idx < prices.length) {
            leadPrice = prices[idx];

            if (buyPrice == -1 && lagPrice < leadPrice) {
                buyPrice = lagPrice;
            } else if (buyPrice != -1 && lagPrice > leadPrice) {
                totalEarnings += (lagPrice - buyPrice);
                buyPrice = -1;
            } else if (buyPrice != -1 && idx == prices.length - 1 && leadPrice > buyPrice) {
                totalEarnings += (leadPrice - buyPrice);
                buyPrice = -1;
            }

            idx++;
            lagPrice = leadPrice;
        }   

        return totalEarnings;
    }
}

class StockSolution {
    public static void main(String[] args) {
        StockSolution1 sol = new StockSolution1();
        int[] prices = {1,2,3,4,5};
        System.out.println(sol.maxProfit(prices));
    }
}