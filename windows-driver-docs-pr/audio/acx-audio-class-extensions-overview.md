---
title: ACX audio class extensions overview
description: This topic provides a high level overview of the ACX Audio Class Extensions.
ms.date: 09/29/2023
ms.localizationpriority: medium
---

# ACX audio class extensions overview

This topic provides a high level summary of the ACX Audio Class Extensions.

### ACX framework is built on top of the Windows Driver Framework

To allow audio drivers to be more reliable and offer the best possible experience for PC users, Audio Class eXtension (ACX) is now available in early preview. ACX defines a new Windows Driver Framework (WDF) class extension for the audio domain. For more information about WDF see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md). Many WDF concepts such as WDF IO targets, are available in ACX. For more information about WDF IO targets, see [Introduction to I/O Targets](../wdf/introduction-to-i-o-targets.md).

ACX is built using the Kernel Mode Driver Framework (KMDF) and not the User Mode Driver Framework (UMDF) to avoid any latency associated with task-switching multiple times from User to Kernel mode while streaming. Portcls audio drivers, the current legacy model, are WDM, kernel mode based drivers.

The use of the ACX framework makes it easy to create working audio drivers ‘out of the box’. For example, ACX  supports default completion for most of its settings. This makes it easier for the driver to use the correct setting, yet still allows for customization.

The ACX framework exposes audio concepts as WDF objects that driver can interact with (stream, format, etc.). This allows for a consistent programming experience and enables a larger community of audio driver developers.

>[!NOTE]
> The ACX headers and libraries are not included in the  WDK 10.0.22621.2428 (released October 24, 2023), but are available in previous versions, as well as the latest (25000 series builds) Insider Preview of the WDK. For more information about preview versions of the WDK, see [Installing preview versions of the Windows Driver Kit (WDK)](../installing-preview-versions-wdk.md).

### ACX goals

The audio class extensions (ACX) have the following goals.

- Simplify the effort and know-how required to develop simple stand-alone audio drivers.
- Reduce the amount of code that a 3rd party needs to develop. Fewer lines of code decreases maintenance and makes debugging easier.
- Allows existing upper user-mode clients (services and apps) to run as is.
- Simplify the power-pnp management of the audio stack drivers.
- No impact the overall performance, i.e., no additional/noticeable latency.
- Simplify the effort required to develop multi-stack audio drivers.
- Allow 3rd party driver to specify the locking mechanism to be used when streaming.
- Uses the Microsoft component deployment isolation solution that makes drivers/APOs modules self-contained and reusable.

### ACX architecture

This diagram illustrates the ACX architecture showing existing user mode apps and ACX objects in kernel mode and audio hardware at the bottom of the stack. In addition to the ACX objects, the driver developer has access to the WDF objects to take advantage of in their driver code, for example for power management.

:::image type="content" source="images/audio-acx-architecture-overview.png" alt-text="Diagram illustrating the ACX architecture, showing user and kernel mode with WDF and ACX objects in kernel mode, and audio hardware at the bottom of the stack.":::

### ACX coexistance with existing audio drivers

ACX is designed to co-exist with existing audio drivers, to allow for a flexible migration to new ACX drivers.

- Binary compatibility of exiting, unchanged (WDM-based) audio miniport drivers is maintained by existing legacy Windows class drivers. 
- Only WaveRT based streaming is currently supported by ACX.
- Legacy PortCls/Ks and new ACX stacks run side-by-side. Using ACX does not force 3rd party to port their current audio drivers to the new model. As the model offers many advantages, 3rd parties may voluntarily opt to use it for their future audio development.

## ACX common definitions

*Circuit* - A driver component representing a partial or full audio path. The circuit represents an existing endpoint and its capabilities.

*Stream* -  A driver component that’s created to represent an audio stream, created by a Circuit. The Stream is composed of a list of Elements created based on the parent Circuit’s Elements.  

*Stream Circuit* - the circuit in a multi-stack architecture (partial audio path) that directly interface with upper user-mode streaming service.

*Core Circuit* - The circuit in a multi-stack architecture (partial audio path) that gives the identity of the audio endpoint device.

*Element* - A subcomponent of a Circuit or Stream, representing an audio capability of the underline hardware. This could be a Volume, or Mute, or Jack element, or a Module element on a DSP circuit, etc.

*Endpoint Audio Path* - A single or group of Circuit objects connected together to represent a single audio endpoint. The Circuit objects must come from different device stacks belonging to the same or different drivers.

### Summary of ACX objects

For a summary of the base ACX objects, see [Summary of ACX objects](acx-summary-of-objects.md).

## Sample ACX driver

A simple ACX sample driver is available to view and download on GitHub in the develop branch - [https://github.com/microsoft/Windows-driver-samples/tree/develop/audio/Acx/Samples](https://github.com/microsoft/Windows-driver-samples/tree/develop/audio/Acx/Samples).

## Driver Verifier

The use of driver verifier is encouraged for all Windows drivers, including ACX drivers. Use driver verifier to surface latent errors, decrease the power consumption and increase the reliability of your driver. For more information, see [Driver Verifier](../devtest/driver-verifier.md).

## ACX Multi-stack driver standardized cross communications

It is common for the audio path to go through multiple hardware components handled by different driver stacks to create a complete audio experience.  It is typical for a system to have the DSP, CODEC and AMP functionality implemented by different audio technology vendors.

In a multi-stack architecture without a well-defined standard, each vendor is forced to define its own proprietary interface and communications protocol. It is a goal of ACX to facilitate the development of multi-stack audio drivers by taking ownership of the synchronization between these stacks and providing a simple re-usable pattern for drivers communicate with each other.

For more information, see [ACX multi stack cross driver communications](acx-multi-stack.md).

## ACX reference documentation

For information about the header level ACX reference documentation, see [ACX reference documentation](acx-reference.md).

## See also

[Summary of ACX objects](acx-summary-of-objects.md)

[ACX reference documentation](acx-reference.md)

[ACX version information](acx-version-overview.md)

[ACX logging and debugging](acx-logging-and-debugging.md)

[ACX targets and driver synchronization](acx-targets.md)

[ACX IO request packet IRPs](acx-irps.md)

[ACX device enumeration](acx-device-enumeration.md)

[ACX power management](acx-power-management.md)

[ACX multi stack cross driver communications](acx-multi-stack.md)

[ACX streaming](acx-streaming.md)
