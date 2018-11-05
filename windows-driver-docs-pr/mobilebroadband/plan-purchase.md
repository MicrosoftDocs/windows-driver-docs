---
title: Plan purchase
description: Plan purchase
ms.assetid: e4713e66-a26d-4408-885e-877259e4450b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plan purchase


A simple and intuitive on-device plan purchase that is integrated with the Windows experience can simplify the subscription acquisition process and let users purchase the subscription when they need the mobile connectivity.

Developing a plan purchase experience involves the following:

-   **Determination of subscription status** When the app is started, it should intelligently determine whether the device has a currently associated plan, and then show the appropriate experience based on that. For existing users who have no current associated plan, the app can show an Account Management experience and a Purchase Subscription experience.

    To determine the current subscription status, the mobile broadband app can get device and subscription information from Windows — for example, International Mobile Subscriber Identity (IMSI), Integrated Circuit Card ID (ICCID), and International Mobile Equipment Identity (IMEI). It can use the connectivity status of mobile broadband connection to determine whether the user has a plan.

-   **Purchase or top-up experience** The purchase business-logic details (such as plan information, payment, and credit card validation) must be maintained in your app. Windows supports web services or cellular protocols such as Unstructured Supplementary Service Data (USSD) to interact with your back-end systems to develop this business logic.

-   **Provisioning** After the user has purchased the plan, Windows must provision the device and you must activate the device in its back-end. Provisioning is defined as configuring a Windows-based computer with information that is required to connect to a carrier network. This typically occurs after a subscription purchase. Provisioning information contains mobile broadband profile (access point name \[APN\], user name, and password), hot-spot profiles, Wi-Fi credentials, and plan information. Windows can use this information to automatically connect to your network without any user input. 

For more info about provisioning, see [Account provisioning](account-provisioning.md).

For some carriers, the activation process on the mobile network is not instantaneous and can take up to ten minutes. Your app must handle this case elegantly and give a good user experience. The Windows activation experience should get information about estimated activation time and display that information to the user during the purchase.

Design considerations include the following:

-   **Simplify the user experience by retrieving device information** During a purchase, your business logic needs device information to show the plans that are available for the device. Your app can get the information by using the [Subscriber and Device Information API](subscriber-and-device-information-api.md); therefore, you don’t have to ask the user to manually enter this information.

-   **Provide a seamless connection experience by using the Provisioning API** After the user has purchased the plan, you can assign credentials to the subscription. The user must use these credentials and connectivity parameters to connect to your network. You can use the [Provisioning API](provisioning-api.md) to provide this information. The Provisioning Engine will store this information and automatically connect to your network.

-   **Choose the back-end interaction** For purchasing the plan, the user can use limited connectivity, alternate Internet connectivity (home, coffee shop), or control channel protocols (USSD).

The following flow chart describes how plan purchase works with Windows and UWP apps:

![plan purchase flowchart](images/mb-fig1-planpurchaseflowchart.png)

## <span id="related_topics"></span>Related topics


[Mobile broadband app scenarios](mobile-broadband-app-scenarios.md)

 

 






