---
title: Voice Allocation
description: Voice Allocation
ms.assetid: fb1e6c36-02b4-41a6-b9c4-09f393d389db
keywords: ["DirectMusic kernel-mode WDK audio , voice allocation", "kernel-mode synths WDK audio , voice allocation", "voice allocation WDK audio", "hardware acceleration WDK audio", "miniport drivers WDK audio , kernel-mode hardware acceleration", "synthesizers WDK audio , kernel-mode hardware acceleration", "synthesizers WDK audio , voice allocations"]
---

# Voice Allocation


## <span id="voice_allocation"></span><span id="VOICE_ALLOCATION"></span>


Most adapter drivers that contain a synthesizer miniport driver also contain DirectSound hardware acceleration. This brings up the question of voice allocation between synthesizer voices and hardware-accelerated DirectSound buffers.

DirectMusic synths--both hardware and software--should support multiple instances in order to maximize the number of concurrent clients. A synth writer might be tempted to statically allocate voices to synths, but should probably consider all available instances of synths as drawing from a common, dynamic voice pool. Each instance then reports the available number of voices as the total number available in the pool.

When implemented this way, even a hardware synth with a limited number of physical voices can support numerous synth instances. In real time, the STATS call informs the client of how many voices each instance is currently using. If the dynamic pool is depleted and a synth instance requires a new voice, then that synth instance must implement a voice-stealing scheme to free a voice from within that instance.

The following allocation scheme is based on the idea that voices used by a synthesizer are more easily shared than DirectSound buffers because the driver has control over what data goes in what voice and can make decisions about voice stealing (outlined in the DLS Level 1 specification).

All of the voices available to the miniport driver (hardware, software, or some combination of hardware and software) are divided into two pools. The first pool, the free pool, consists of voices that are not committed anywhere. The second pool, the dynamic pool, consists of voices that are committed to use by synthesizer instances. These voices may or may not currently be in use by a synthesizer instance. The dynamic pool is sized as the maximum number of voices requested by any synthesizer instance, subject to the current contents of the free pool. DirectSound buffers are removed from the free pool upon allocation and returned on deallocation.

The following table contains an example sequence of voice allocations that illustrate the scheme in practice.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Time</th>
<th align="left">Request</th>
<th align="left">Free Pool</th>
<th align="left">Dynamic Pool</th>
<th align="left">Miniport Driver Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>T0</p></td>
<td align="left"><p>Power Up</p></td>
<td align="left"><p>64</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Initialize.</p></td>
</tr>
<tr class="even">
<td align="left"><p>T1</p></td>
<td align="left">DSound
(4)</td>
<td align="left"><p>60</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Statically allocate four voices to DirectSound buffers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>T2</p></td>
<td align="left">Synth
(32)</td>
<td align="left"><p>28</p></td>
<td align="left"><p>32</p></td>
<td align="left"><p>Increase dynamic pool to 32 voices.</p></td>
</tr>
<tr class="even">
<td align="left"><p>T3</p></td>
<td align="left">Synth
(24)</td>
<td align="left"><p>28</p></td>
<td align="left"><p>32</p></td>
<td align="left"><p>No action. There are already more than 24 voices in the dynamic pool.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>T4</p></td>
<td align="left">DSound
(24)</td>
<td align="left"><p>4</p></td>
<td align="left"><p>32</p></td>
<td align="left"><p>Statically allocate 24 voices to DirectSound buffers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>T5</p></td>
<td align="left">Synth
(48)</td>
<td align="left"><p>0</p></td>
<td align="left"><p>36</p></td>
<td align="left"><p>Increase dynamic pool to 36 voices. (The method that creates the port returns S_FALSE and sets DMUS_PORTPARAMS.<strong>dwVoices</strong> = 36.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>T6</p></td>
<td align="left">DSound
(10)</td>
<td align="left"><p>0</p></td>
<td align="left"><p>36</p></td>
<td align="left"><p>Fail. No voices in free pool.</p></td>
</tr>
<tr class="even">
<td align="left"><p>T7</p></td>
<td align="left">DSound
(-5)</td>
<td align="left"><p>5</p></td>
<td align="left"><p>36</p></td>
<td align="left"><p>Free five voices. Note that these do not go back into the dynamic pool, even though the last request (at time T5) was for more than were granted.</p></td>
</tr>
</tbody>
</table>

 

Note that DirectSound buffers are actually allocated one by one, and are grouped together in the table for the purpose of readability.

Immediately after a synthesizer pin instance is created, no voices should be allocated based on it. Shortly after creation, a [**KSPROPERTY\_SYNTH\_PORTPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff537405) property item is received. This property item indicates, among other things, the number of voices that are to be associated with this instance. This item also gives the miniport driver the chance to report back the actual new size of the dynamic pool in case all requested voices could not be allocated.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Voice%20Allocation%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




