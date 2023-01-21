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

    const timelineEvents = [
        {
            title: 'Wael and Tony Meet',
            date: 'February 2021',
            details: 'Kicking around ideas on the Arming Cardano Telegram channel',
            faIcon: 'fa-handshake-simple',
            faStyle: 'color:rgb(205, 35, 85);',
            height: '150px'
        },
        {
            title: 'Catalyst Fund4: ARMing Cardano',
            date: 'March 2021',
            details: 'Creating SPO content for ARM devices',
            faIcon: 'fa-lightbulb',
            faStyle: 'color:Navy;',
            height: '175px'
        },
        {
            title: 'PIADA Registered on Mainnet',
            date: 'March 15th, 2021 04:29 AM UTC',
            details: 'Four Raspberry Pis and no fear (and maybe some beer)',
            faIcon: 'fa-bullhorn',
            faStyle: 'color:rgb(205, 35, 85);',
            height: '195px'
        },
        {
            title: 'PIADA 1st Mainnet Block',
            date: 'March 22nd, 2021 08:24 AM UTC',
            details: 'Ouroboros rewards a new pool',
            faIcon: 'fa-cube',
            faStyle: 'color:Green;',
            height: '150px'
        },
        {
            title: 'Innerview with KEWW - Ken Adams',
            date: 'April 2021',
            details: 'Three people, two new projects and a lotta stoke',
            faIcon: 'fa-microphone-lines',
            faStyle: 'color:Goldenrod;',
            height: '195px'
        },
        {
            title: 'Armada Alliance is Born',
            date: 'April 2021',
            details: 'A group of ARM enthusiasts start a movement',
            faIcon: 'fa-skull-crossbones',
            faStyle: '',
            height: '150px'
        },
        {
            title: 'Cardano Foundation Delegation',
            date: 'July 2021',
            details: 'Putting the PIADA Raspberry Pis to the test',
            faIcon: 'fa-rocket',
            faStyle: 'color:rgb(72, 127, 255);',
            height: '150px'
        },
        {
            title: 'Catalyst Fund6: Cardano-Heartbeat (CEM)',
            date: 'August 2021',
            details: 'Protecting the Cardano network from disasters',
            faIcon: 'fa-lightbulb',
            faStyle: 'color:Navy;',
            height: '195px'
        },
        {
            title: 'PIADA 100th Mainnet Block',
            date: 'August 24th, 2021 6:33 AM UTC',
            details: 'Small hardware, big milestone',
            faIcon: 'fa-cube',
            faStyle: 'color:Green;',
            height: '150px'
        },
        {
            title: 'Catalyst Fund8: Cardano Tools & Software for ARM',
            date: 'March 2022',
            details: 'Armada Alliance OGs leveling up',
            faIcon: 'fa-lightbulb',
            faStyle: 'color:Navy;',
            height: '195px'
        },
        {
            title: 'Cardano Foundation Delegation',
            date: 'July 2022',
            details: 'Whale hello again',
            faIcon: 'fa-rocket',
            faStyle: 'color:rgb(72, 127, 255);',
            height: '150px'
        },
        {
            title: 'Wael Meets Charles at cNFTcon',
            date: 'October 2022',
            details: 'Just two visionaries rubbing elbows',
            faIcon: 'fa-thumbs-up',
            faStyle: 'color:rgb(205, 35, 85);',
            height: '175px'
        },
        {
            title: 'Cardano Foundation Delegation',
            date: 'October 2022',
            details: 'Testing new hardware and tweaking some automation',
            faIcon: 'fa-rocket',
            faStyle: 'color:rgb(72, 127, 255);',
            height: '150px'
        }
    ]
</script>

<div class="w3-container" style="padding:128px 2px" id="timeline">
    <h2 class="w3-center" style="padding-bottom:20px;">OUR STORY</h2>
    <Timeline position="alternate">
        {#each timelineEvents as te}
        <TimelineItem>
            <TimelineOppositeContent slot="opposite-content">
                <p>{te.date}</p>
            </TimelineOppositeContent>
            <TimelineSeparator>
                <TimelineDot style={'width: 45px; height: 48px; background-color: #fff; display: flex; justify-content: center; border-color: transparent;'}>
                    <i class="fa-solid {te.faIcon} fa-beat-fade w3-margin-bottom w3-xxlarge" style="--fa-animation-duration: 2s; --fa-beat-fade-opacity: 0.67; --fa-beat-fade-scale: 1.055; {te.faStyle}"></i>
                </TimelineDot>
                <TimelineConnector />
            </TimelineSeparator>
            <TimelineContent style={'line-height:1.6em;height:' + te.height + ';'}>
                <h3>{te.title}</h3>
                <p>{te.details}</p>
            </TimelineContent>
        </TimelineItem>
        {/each}
    </Timeline>
</div>