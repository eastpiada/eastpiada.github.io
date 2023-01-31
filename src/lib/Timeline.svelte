<script>
    import {
		Timeline,
		TimelineItem,
		TimelineSeparator,
		TimelineDot,
		TimelineConnector,
		TimelineContent,
		TimelineOppositeContent
	} from 'svelte-vertical-timeline';
    import storyData from '$lib/data/storyData.json';
</script>

<div class="w3-container" style="padding:128px 2px" id="timeline">
    <h2 class="w3-center" style="padding-bottom:20px;">OUR STORY</h2>
    <Timeline position="alternate">
        {#each storyData as sd}
        <TimelineItem>
            <TimelineOppositeContent slot="opposite-content">
                <p>{sd.date}</p>
            </TimelineOppositeContent>
            <TimelineSeparator>
                <TimelineDot style={'width: 45px; height: 48px; background-color: #fff; display: flex; justify-content: center; border-color: transparent;'}>
                    <i class="fa-solid {sd.faIcon} fa-beat-fade w3-margin-bottom w3-xxlarge" style="--fa-animation-duration: 2s; --fa-beat-fade-opacity: 0.67; --fa-beat-fade-scale: 1.055; {sd.faStyle}"></i>
                </TimelineDot>
                <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent style={'line-height:1.6em;height:' + sd.height + ';'}>
                <h3>{sd.title}</h3>
                <p>{sd.details}</p>
            </TimelineContent>
        </TimelineItem>
        {/each}
    </Timeline>
</div>