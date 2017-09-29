---
title: Threat modeling for drivers
description: Driver writers and architects should make threat modeling an integral part of the design process for any driver. This article provides guidelines for creating threat models for drivers for the Microsoft Windows family of operating systems.
ms.assetid: 77FB242E-A07C-4298-80ED-866F8D80118C
ms.author: windowsdriverdev
ms.date: 06/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Threat modeling for drivers

Driver writers and architects should make threat modeling an integral part of the design process for any driver. This article provides guidelines for creating threat models for drivers for the Microsoft Windows family of operating systems.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[Create threat models for drivers](threat-models-for-drivers-create.md)</p></td>
<td align="left"><p>Creating a threat model requires a thorough understanding of the driver’s design, the types of threats to which the driver might be exposed, and the consequences of a security attack that exploits a particular threat. After creating the threat model for a driver, you can determine how to mitigate the potential threats.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Points to consider regarding threat modeling for drivers](threat-modeling-for-drivers-points-to-consider.md)</p></td>
<td align="left"><p>This topic discusses points to consider regarding threat modeling for drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Call to action and resources (threat modeling for drivers)](threat-modeling-for-drivers-call-to-action.md)</p></td>
<td align="left"><p>This article contains call to action recommendations and resources for threat modeling for drivers.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Introduction"></span><span id="introduction"></span><span id="INTRODUCTION"></span>Introduction


Security should be a fundamental design point for any driver. Any successful product is a target. If you are writing a driver for Microsoft Windows operating systems, you must assume that sometime, somewhere, someone will try to use your driver to compromise system security.

Designing a secure driver involves:

-   Identifying the points at which the driver could be vulnerable to an attack.
-   Analyzing the types of attacks that could be mounted at each such point.
-   Ensuring that the driver contains features to prevent or thwart such attacks.

Threat modeling is a structured approach to these important design tasks. A threat model is a way of categorizing and analyzing the threats to an asset. From a driver writer’s perspective, the assets are the hardware, software, and data on the computer or network.

A threat model answers the following questions:

-   Which assets need protection?
-   To what threats are the assets vulnerable?
-   How important or likely is each threat?
-   How can you mitigate the threats?

Threat modeling is an important part of software design because it ensures that security is built into the product, rather than addressed as an afterthought. A good threat model can help find and prevent bugs during the design process, thus eliminating potentially costly patches later and possible reputational damage to your organization.

This section applies the principles of threat modeling to driver design and provides examples of threats to which a driver might be susceptible. For a more complete description of threat modeling for software design, refer to these resources.

-   The Microsoft SDL Web site:

    <http://www.microsoft.com/sdl>

-   Simplified Implementation of the Microsoft SDL:

    [Download White Paper](http://go.microsoft.com/?linkid=9708425)

-   This blog describes how to download a free copy of *The Security Development Lifecycle: SDL*, by Michael Howard and Steve Lipner:

    <https://blogs.msdn.microsoft.com/microsoft_press/2016/04/19/free-ebook-the-security-development-lifecycle/>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Threat%20modeling%20for%20drivers%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




