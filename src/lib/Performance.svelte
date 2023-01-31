
<script>
    import perfData from '$lib/data/poolData.json';
</script>

<div class="w3-container" style="padding:64px 2px" id="performance">
    <div class="w3-row w3-center w3-green w3-padding-64">
        <div class="w3-col m2">
            <span class="w3-xxlarge">{perfData.total_delegated}</span>&#8371;<br>
            Pool Delegation
        </div>
        <div class="w3-col m2">
            <span class="w3-xxlarge">{perfData.pledge}</span>&#8371;<br>
            Pool Pledge
        </div>
        <div class="w3-col m2">
            <span class="w3-xxlarge">{perfData.block_count}</span><br>
            Lifetime Pool Blocks
        </div>
        <div class="w3-col m2">
            <span class="w3-xxlarge">{perfData.ten_epoch_ros}%</span><br>
            10 Epoch Return on Stake
        </div>
        <div class="w3-col m2">
            <span class="w3-xxlarge">{perfData.pool_fee}%</span><br>
            Low Variable Pool Fee
        </div>
        <div class="w3-col m2">
            <span class="w3-xxlarge">{perfData.delegate_rewards}</span>&#8371;<br>
            Lifetime Rewards to Delegates
        </div>
    </div>
</div>

<style>
    .w3-col {text-shadow:1px 1px 4px #000;}
</style>