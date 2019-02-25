---
title: Tap and Do use cases
description: Tap and Do use cases
ms.assetid: DCA97F86-3D27-46CD-9D25-A3D156B18B85
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tap and Do use cases


Windows provides several use cases to support the *Tap and Do* gesture. Each use case initiates a particular action between devices. The following table lists the use cases available.

 

| Use case          | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Tap and Setup     | Tap and pair to setup a peripheral wireless device with Windows.            |
| Tap and Reconnect | Tap and reconnect a previously paired and setup device with Windows.        |
| Tap and Use       | Tap and connect your app with one running on another machine.               |
| Tap and Launch    | Tap and invite a user on another machine to launch an app your are running. |
| Tap and Acquire   | Tap and invite a user on another machine to obtain an app your are running. |
| Tap and Send      | Tap and send content you have selected to another device.                   |
| Tap and Receive   | Tap and receive content from another device or poster.                      |

 

## Categorization


NFP use cases generally belong in one of two categories.

-   *Personal*

    This category of use cases involves the user of the system only.

    -   No other person is involved.
    -   The user is directly manipulating the Windows system with another device such as a tag, a card, a peripheral wireless device, or a smaller smart device such as a mobile phone.
    -   The user has complete control over the use case from trust, confidence, and physical perspectives.
-   *Interpersonal*

    This category of use cases involves two users working together, with at least one user using a Windows system.

    -   Another user is always involved.
    -   The other user may also be using a Windows system, or he may be using another device such as a mobile phone.
    -   The two users must work cooperatively to carry out the use case. That includes aligning the devices to trigger actions to occur.

## Tap and Setup


*Tap and Setup* is a wireless device installation experience for peripheral devices. The category includes keyboards, mice, headphones, and printers. Tap and setup supports three different types of device installations: Bluetooth unidirectional pairing, network printer installation, and Wi-Fi Direct printer pairing. Windows will only install devices, which support unidirectional communication over NFC. Smart devices that require bidirectional communication over NFC are not supported. Using this experience, a user can tap compatible devices to Windows to initiate the device setup experience.

Use category: personal or enterprise (interpersonal).

**Use case example**

1.  An NFP-enabled device is placed near a computer to trigger device setup.
2.  Windows detects the device and presents a toast user interface (UI) inviting the user to proceed with installing the device. If the user accepts, device pairing and setup proceed. If the user declines, pairing does not occur and device setup does not proceed. In such a case, the user must tap again to initiate pairing if desired.
3.  When device setup has finished, Windows may invoke AutoPlay if specified by the device. Otherwise, no device experience is shown.

## Tap and Reconnect


*Tap and Reconnect* is a wireless connection experience for peripheral devices supporting the *Tap and Setup* scenario. Using this experience, a user can tap compatible devices to Windows to reestablish the connection with the computer that has already been set up with the computer using the *Tap and Setup* use case. This use case is typical for peripherals that cannot remember more than one pairing relationship and that are used across multiple machines.

Use category: personal.

**Use case example**

1.  An NFP-enabled device is placed near a computer to trigger device reconnection.
2.  Windows detects the device and presents a toast UI inviting the user to proceed with installing the device. If the user accepts, device pairing proceeds. If the user declines, pairing does not occur. In such a case, the user must tap again to initiate pairing if desired.
3.  When device pairing has finished, Windows may invoke AutoPlay if specified by the device. The user’s previous choice will be remembered. Otherwise, no device experience is shown.

## Tap and Use


*Tap and Use* is a developer experience that supports using an API to trigger collaboration between apps running on two different computers. A user running an app on his computer that is enabled for NFP will be able to trigger collaboration with the same app running on another machine when the two users tap their machines together. The API can also be used with compatible apps and compatible apps on machines other than the computer, where compatibility is handled through the underlying NFP technology.

Use category: personal or interpersonal.

**Use case example**

1.  A user wants to play a game with his friend. He starts the app and so does she. The apps are designed for NFP. The app may prompt both users to tap their computers together.
2.  Once the users tap their computers together, the API is triggered and information set to be transmitted is exchanged between the computers. That may include setting up a channel over a wireless link so that the apps are able to communicate with each other.

## Tap and Launch


*Tap and Launch* is an interaction for launching apps. A user running an app that is enabled for NFP can invite another user to run the same app by tapping his computer to another device. The second user will be invited to launch the same app.

Use category: personal or interpersonal.

**Use case example**

1.  A user wants to play a game with his friend. He starts the app and so does she. The apps are designed for NFP. The app may prompt both users to tap their computers together.
2.  The second user is not running the app but has it installed. She is invited to launch the app. If she declines the invitation, nothing happens.
3.  If she accepts the invitation, the app starts. The users are now able to play the game together.

## Tap and Acquire


*Tap and Acquire* is an interaction for app acquisition. Using this experience, a user running an app on his computer will be able to invite a friend to obtain the same app if they do not have it installed.

Use category: personal or interpersonal.

**Use case example**

1.  A user wants to play a game with a friend. He starts the app. The app may prompt him to tap his computer to another computer.
2.  The second user does not have the app installed. She is invited to acquire the app he is inviting her to use. If she declines the invitation, nothing happens.
3.  If she accepts the invitation, she can acquire the app. The app will not start automatically. To do that, she will either need to run it directly and tap again with her friend (the *Tap and Use* use case), or simply tap again with her friend to launch the app (the *Tap and Launch* use case).

## Tap and Acquire


*Tap and Acquire* is an interaction for app acquisition. Using this experience, a user running an app on his computer will be able to invite a friend to obtain the same app if they do not have it installed.

Use category: personal or interpersonal.

**Use case example**

1.  A user wants to play a game with a friend. He starts the app. The app may prompt him to tap his computer to another computer.
2.  The second user does not have the app installed. She is invited to acquire the app he is inviting her to use. If she declines the invitation, nothing happens.
3.  If she accepts the invitation, she can acquire the app. The app will not start automatically. To do that, she will either need to run it directly and tap again with her friend (the *Tap and Use* use case), or simply tap again with her friend to launch the app (the *Tap and Launch* use case).

## Tap and Send


*Tap and Send* is a content-sharing interaction. Using this experience, a user can tap his computer to another device to send content such as the URL of a webpage, a document, or a collection of pictures.

Use category: personal or interpersonal.

**Use case example**

1.  A user viewing a web page within an Internet browser on his computer taps his computer to the computer of another user.
2.  The sending user is presented with a UI to send the URL of the webpage he’s viewing.
3.  He sees that his friend has accepted the content transfer and transfer UI is presented.

## Tap and Receive


*Tap and Receive* is an interaction for users to receive content. Using this experience, a user can tap his computer to another device (such as a computer or phone) or object (such as a tag) that is sharing content. Windows will initiate a receive experience upon user confirmation to help the user obtain and make use of the received content.

Use category: personal or interpersonal.

**Use case example**

1.  A user taps her computer to a device her friend is holding that is sharing content. Or she taps her computer against a poster on a wall that contains an embedded tag. The tag has content available to be read.
2.  She is invited to receive the content. If she declines the invitation, nothing happens. If she accepts the invitation, she is presented with the progress of the receive action.
3.  Once the content is received, she is then invited to launch an app to handle the content. The app is launched and handed the content.

 

 





