---
title: Tap and Do scenarios
description: Tap and Do scenarios
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 06/08/2020
---

# Tap and Do scenarios

*Tap and Do* is a gesture that is a natural interaction between people in close proximity used to trigger doing something together between the devices they are holding.

Starting with Windows 8, a new gesture is introduced for real world interaction called *Tap and Do*. *Tap and Do* works within a narrow physical volume (on the order of centimeters) so it is very intentional. A programming model maps this intentionality to the triggering of actions between devices within the physical environment. The underlying system of Near Field Proximity (NFP) is primarily modeled on technologies that use electromagnetic fields, such as NFC, but the platform is flexible and other innovative systems that meet the NFP requirements are supported. Windows provides a user model based on NFP that is easy to understand, lightweight, and intuitive. Windows includes with a number of built-in experiences that leverage NFP. The API is available for third-party development.

There are two user scenarios areas supported for *Tap and Do* in Windows.

## Peripheral Wireless Device Setup

Before users can use peripheral devices with Windows, they must logically connect, pair, and setup the devices on the computer. They can do this either with cables or over a wireless network.

While using cables is intuitive and effective, this often give a poor user experience because people don’t typically carry cables with them to stay connected. Meanwhile, pairing a peripheral wireless device with Windows can be a multi-step task requiring device discovery and authentication.

With Tap and Do, the user just taps the peripheral wireless device to the computer. This single action works to trigger the automatic wireless setup of the device without any other steps. The simplicity of this experience eliminates common user difficulties associated with device setup.

## Ad-Hoc Interaction in the Real World

Windows does not provide a common way for users to interact with other users or the physical environment through their devices. For one user to discover another user immediately nearby, and to interact with what they are doing, both users must typically connect through apps that have a proprietary rendezvous mechanism through the Internet. This approach typically requires a preexisting relationship for each user with the app or service in question, and also typically requires the users to exchange some kind of identifier with each other in order to support the rendezvous.

With *Tap and Do*, the users just tap their computers together to create the relationship and trigger further actions appropriate to the context of what the users are doing. This simple action can initiate complex interactions between the computers. It can be used to exchange simple information, such as a URL. It can be used to trigger the sharing of more complex information on an alternative wireless transport. One example is the exchange pictures or a document over Wi-Fi. Also, it can be used by apps to exchange app-specific information, such as the identity and address information necessary to trigger activities between an app running on both computers as well as services on the Internet.

A user can also use this gesture to communicate with other devices within their own environment. For example, reading a tag on a poster or passing information from their computer to their phone or vice-versa.

See [Tap and Do Use Cases](tap-and-do-use-cases.md) for and explanation of various device interactions with the *Tap and Do* gesture.

## Related topics

[NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)  

[Near field proximity DDI reference](/windows-hardware/drivers/ddi/_nfpdrivers)
