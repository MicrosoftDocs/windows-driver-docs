---
Description: 'Implementation of Function-Specific Interfaces'
MS-HAID: 'audio.implementation\_of\_function\_specific\_interfaces'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: 'Implementation of Function-Specific Interfaces'
---

# Implementation of Function-Specific Interfaces


## <span id="implementation_of_function_specific_interfaces"></span><span id="IMPLEMENTATION_OF_FUNCTION_SPECIFIC_INTERFACES"></span>


A typical audio adapter card contains a collection of audio hardware functions, which the adapter driver can expose to the WDM audio system through a corresponding collection of IMiniport*Xxx* interfaces. All IMiniport*Xxx* interfaces inherit from [IMiniport](audio.iminiport). Each type of miniport interface--wave, MIDI, topology, and so on--encapsulates a miniport driver for controlling a particular type of audio function on an adapter card. A driver can also expose several instances of the same miniport interface to represent multiple instances of the same (or similar) hardware functions.

For more information, see [Miniport Interfaces](miniport-interfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Implementation%20of%20Function-Specific%20Interfaces%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



