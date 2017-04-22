---
title: Handling Existing Monitor Configurations
description: Handling Existing Monitor Configurations
ms.assetid: b2da12ea-cbcd-4754-a65f-e54ed305f5d7
keywords:
- monitor configurations WDK display , restore previous
- monitor configurations WDK display , existing monitors
- TMM WDK display , existing monitor configurations
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Existing Monitor Configurations


Besides detecting new monitors and launching the TMM dialog in a two-monitor configuration, TMM also must restore previous display configurations. TMM can restore display configurations by passing display data to the user-mode display driver through the [**IViewHelper::SetConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff568176) method. TMM will allocate memory and store display modes and topology information in the memory. TMM passes this memory in an **IStream** interface that the *pIStream* parameter of **SetConfiguration** points to. The user-mode display driver can also modify or fold in other display data (for example, gamma or TV settings). When the driver is finished with the display data, the driver calls the **IStream::Release** method to free the memory.

The following figure shows the flow of operations that occur when TMM restores an existing monitor configuration.

![diagram illustrating restoring an existing monitor configuration](images/tmm-existconfig.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Existing%20Monitor%20Configurations%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




