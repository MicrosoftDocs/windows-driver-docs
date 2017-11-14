---
title: Windows Dev Center for Data Marketplace
author: windows-driver-content
description: This topic describes Windows Dev Center for Data Marketplace.
ms.assetid: 1D9C09AC-06D0-43F5-B2EC-9833B1A2383D
keywords:
- Data Marketplace mobile operators, Data Marketplace mobile broadband WDK
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows Dev Center for Data Marketplace

To offer connectivity offers in a Windows Store pay-as-you-go (PAYG) scenario, you need to publish your Windows app through Dev Center. This app does not need to provide any real functionality. It is a container app function as the vehicle to supply your branding elements and the connectivity offers that you want to sell through Windows Store as add-ons associated with your container app. The app doesn&#39;t need to be visible or used by customers, but it must be listed in Windows Store. Your offers will be presented to the customer within the [Paid Wi-Fi and Cellular app](https://www.microsoft.com/store/apps/9NBLGGH5PNB1).

As a Windows Store seller, Windows Dev Center is the main portal to help you plan, build, and market your connectivity offers. To take advantage of all Dev Center capabilities, get familiar with the docs on [packaging Windows apps](https://docs.microsoft.com/en-us/windows/uwp/packaging/packaging-uwp-apps) and [publishing Windows apps](https://docs.microsoft.com/en-us/windows/uwp/publish/). Here is a list of topics you should review before using Dev Center.

| **Topic** | **Description** |
| --- | --- |
| [Using the Windows Dev Center dashboard](https://docs.microsoft.com/en-us/windows/uwp/publish/using-the-windows-dev-center-dashboard) | Learn  [how to register for an account](https://docs.microsoft.com/en-us/windows/uwp/publish/opening-a-developer-account) and get an overview of what you can do in the Dev Center dashboard. |
| [Create your app by reserving a name](https://docs.microsoft.com/en-us/windows/uwp/publish/create-your-app-by-reserving-a-name) | See how to reserve names and find suggestions for choosing a great app name. |
| [Packing App with Visual Studio](https://docs.microsoft.com/en-us/windows/uwp/packaging/packaging-uwp-apps) | To submit your container app, you need to create an appxupload package for it. |
| [App submissions](https://docs.microsoft.com/en-us/windows/uwp/publish/app-submissions) | An app submission includes  [pricing and availability details](https://docs.microsoft.com/en-us/windows/uwp/publish/set-app-pricing-and-availability),  [properties](https://docs.microsoft.com/en-us/windows/uwp/publish/enter-app-properties),  [age ratings](https://docs.microsoft.com/en-us/windows/uwp/publish/age-ratings),  [packages](https://docs.microsoft.com/en-us/windows/uwp/publish/upload-app-packages), and  [Store listing details](https://docs.microsoft.com/en-us/windows/uwp/publish/create-app-store-listings). Your submission will go through the  [certification process](https://docs.microsoft.com/en-us/windows/uwp/publish/the-app-certification-process) before it&#39;s published to the Store. |
| [Add-on submissions](https://docs.microsoft.com/en-us/windows/uwp/publish/add-on-submissions) | Learn how to publish add-ons (in-app products) through the Windows Dev Center dashboard. |
| [Analytics](https://docs.microsoft.com/en-us/windows/uwp/publish/analytics) | Get detailed analytic data for your apps to see how your apps are doing, from how many customers you&#39;ve reached to how they&#39;re using your app and what they have to say about it. You can also find info on app health, ad usage, and more. |
| [App promotion and customer engagement](https://docs.microsoft.com/en-us/windows/uwp/publish/app-promotion-and-customer-engagement) | Promote your app with  [ad campaigns](https://docs.microsoft.com/en-us/windows/uwp/publish/create-an-ad-campaign-for-your-app),  [promotional codes](https://docs.microsoft.com/en-us/windows/uwp/publish/generate-promotional-codes),  [sale pricing](https://docs.microsoft.com/en-us/windows/uwp/publish/put-apps-and-add-ons-on-sale), and more. |
| [Getting paid](https://docs.microsoft.com/en-us/windows/uwp/publish/getting-paid-apps) | Get details about receiving earnings from your apps, add-ons, and Microsoft Advertising. |
| [Store Policies and Code of Conduct](https://msdn.microsoft.com/library/windows/apps/dn764939.aspx) | This section includes the  [Store Policies](https://msdn.microsoft.com/library/windows/apps/dn764944.aspx) and  [App Quality](https://msdn.microsoft.com/library/windows/apps/mt652261.aspx) criteria that apply to Windows apps and content, and the  [Code of Conduct](https://msdn.microsoft.com/library/windows/apps/dn764941.aspx) that developers should follow. |

The following screenshot shows merchandise information and layout of a data provider page (PDP) in the Paid Wi-Fi &amp; Cellular app. Most information on PDP comes from Dev Center and is fully controlled by you.

![Paid Wi-Fi &amp; Cellular app screenshot](BUGBUG NEED IMAGE).

| Element | Title | Description | Source | Localization |
| --- | --- | --- | --- | --- |
| A | Provider Logo | This is the brand logo you provide in the app package. It will be the same logo for all add-ons ingested in the same app. | App package | N/A |
| B | Product Title | This is branding information you provide in the app package. Note you may choose to have this different from your brand name. It will be the same title for all add-ons ingested in the same app. | Dev Center -&gt; Create a new app | Through app submission |
| C | Plan Provider Brand Name | This is the name to be displayed for you as a provider. Note you provide this name to Data Marketplace team directly and you can use whatever name you want. | Send to Data Marketplace by email | Not supported |
| D | Data Plan Price | This is the plan price set by you when ingesting add-ons in Dev Center. Each plan has its own price. | Dev Center -&gt; Offer Submission | N/A |
| E | Data Plan Title | This is the name of the data plan set by you when ingesting add-ons in Dev Center. Each plan has its own title. | Dev Center -&gt; Offer Submission | Through offer submission |
| F | Provider Description | This is text you provide to describe yourself as a provider and is submitted as part of the app submission. | Dev Center -&gt; App Submission | Through offer submission |
| G | Data Plan Details | This is the descriptive text you submit as part of creating your add-ons within dev center. | Dev Center -&gt; Offer Submission | Through offer submission |
| H | Terms of Service | This is the link to the web hosted Terms of Service. | Dev Center -&gt; App Submission | N/A |
| I | Service Provider Name | This is the publisher name you provide in the app package. | Dev Center -&gt; Account Setup | N/A |
| J | Customer Support | This is the link to the web hosted customer support site. | Dev Center -&gt; App Submission | N/A |

In the following sections you will see step-by-step instructions with more details on how to set the various merchandise elements listed in the table above.

## Create a Windows Dev Center account

Windows Dev Center is the portal you will use to manage and publish your connectivity offers and receive payouts. If your company has registered a Dev Center account already, you may use the same account. Otherwise, follow the instructions below to create a new account.

1. Go to [Dev Center](https://developer.microsoft.com/en-us/store/register) and sign up with a **Company** account.
2. Next, [set up a payout account and tax forms](https://msdn.microsoft.com/en-us/windows/uwp/publish/setting-up-your-payout-account-and-tax-forms). Required to sell and to ensure you are paid.
3. Finally, make sure you set the desired Publisher Display Name in Dec Center Account Settings > Contact Info. 

![Set publisher display name in Dev Center Account Settings](BUGBUG NEED IMAGE).

After registering, you may find [Using the Windows Dev Center dashboard](https://msdn.microsoft.com/en-us/windows/uwp/publish/using-the-windows-dev-center-dashboard) useful. The Windows Dev Center dashboard is the portal for managing and submitting your apps and offers.

### Receive payouts

Windows Dev Center requires customers to register a financial account that&#39;s able to receive payouts from revenue generated in the Windows Store.   [This Windows Store documentation](https://msdn.microsoft.com/en-us/library/windows/apps/dn986925.aspx) explains payment.

## Publish an app in Windows Dev Center

An app must be submitted in Windows Dev Center before you can create connectivity offers for Data Marketplace. The app itself is not something with which your customers will interact, but a featureless placeholder app, used as a vehicle for branding elements. The offers you create will only be presented in the Windows pre-installed [Paid Wi-Fi &amp; Cellular app](https://www.microsoft.com/store/apps/9NBLGGH5PNB1).  Your app is the vehicle for the merchandise elements that appear in the Paid Wi-Fi &amp; Cellular app.

### Create an app listing in Windows Dev Center

1. Log in to [Windows Dev Center](https://developer.microsoft.com/en-us/windows).
2. Go to the Dashboard.
3. Click **Create a new app**.
4. [Reserve a name](https://msdn.microsoft.com/en-us/windows/uwp/publish/create-your-app-by-reserving-a-name) and create your app.

### Email Data Marketplace team your account details

Send an email to [datamartpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com) with the following:

1. Your Microsoft Account registered with Windows Dev Center ([youremailaddress@outlook.com](mailto:youremailaddress@outlook.com)).
2. Your app ID in Dev Center. Retrieve your app&#39;s ID from the URL of your app&#39;s Overview page in Dev Center (clicking on your app in the Dev Center dashboard will redirect to the Overview page). In the following example, the string of characters at the end of the URL is your app&#39;s id:
 - https<span></span>://www.microsoft.com/store/apps/9WZDNCRFHVFW
- https<span></span>://www.microsoft .com/store/apps/&lt;string of characters&gt;
3. Continue with the following sections.

> [!NOTE]
> We will inform you when your account is ready to publish connectivity offers.

### Create and build an app package

1. You need Visual Studio, a tool for creating Windows apps. Get [Visual Studio Community](https://www.visualstudio.com/vs/community/) for free.
2. Using Visual Studio, create an app project.   [Create your first app](https://msdn.microsoft.com/en-us/windows/uwp/get-started/your-first-app) demonstrates how to use application templates to create a basic app. Since your app doesn&#39;t need any real functionality, you can also use a placeholder app. To use the placeholder app, download the [&quot;Hello World&quot; app sample](https://code.msdn.microsoft.com/windowsapps/How-to-run-Hello-World-bd5d79ec) and then follow steps (c) and (d) to customize branding. The provider logo displayed in Paid Wi-Fi &amp; Cellular app is your app&#39;s title. The product title that appears next to your logo is your app name. The subsequent instructions highlight where the app&#39;s name and images may be edited.

![This highlights the provider&#39;s logo and product name displayed in the Paid Wi-Fi &amp; Cellular app](BUGBUG NEED IMAGE). Note that they will be the same for all your add-ons (data plans), unless you submit a different app.

3. Add your app&#39;s icon:

- Open your app project in Visual Studio.
- Open the Solution Explorer.
- Drag and drop your app tile images in the Assets folder.
- Within the Solution Explorer open the file Package.appxmanifest.

![Image assets directory in app project](BUGBUG NEED IMAGE).

- Make sure the **Visual Assets** tab in the Package.appxmanifest file is selected.
- Reference the images you dropped in the Assets folder with the app so the images are assigned as the app tile image.
- [This MSDN article](https://msdn.microsoft.com/en-us/windows/uwp/controls-and-patterns/tiles-and-notifications-creating-tiles) shows how an app&#39;s tile may be set. Before creating a tile image, it&#39;s worth reviewing the [Tile and icon asset guidelines](https://msdn.microsoft.com/en-us/windows/uwp/controls-and-patterns/tiles-and-notifications-app-assets).
- &quot;Store Logo&quot; is required for an app to go through certification in Windows Store. It is not used in Paid Wi-Fi and Cellular app.
- &quot;Square 150x150 Logo&quot; is displayed in Paid Wi-Fi &amp; Cellular app. Make sure that the image has a background color other than transparent.
- It is better to add images for all &quot;Scaled Assets&quot;. The more images you have in different sizes, the better chance that a high-resolution image is displayed in Paid Wi-Fi and Cellular app with different app windows sizes.

![Package.appxmanifest file where an app&#39;s tile image can be set](BUGBUG NEED IMAGE)

4. You may [localize](https://msdn.microsoft.com/en-us/windows/uwp/globalizing/put-ui-strings-into-resources) your app&#39;s name by referencing a localized resource as demonstrated in [this MSDN article](https://msdn.microsoft.com/en-us/windows/uwp/globalizing/globalizing-portal) and [this step-by-step instruction](http://www.c-sharpcorner.com/UploadFile/7e39ca/localization-and-globalization-in-windows-store-apps/).
5. Associate your app with the Store and choose the app name you reserved previously.
6. In Visual Studio, right-click on your project and select **Store > Associate App with the Store**.

![Submit an App from Visual Studio](BUGBUG NEED IMAGE)

7. To [build an app package](https://msdn.microsoft.com/en-us/windows/uwp/packaging/packaging-uwp-apps) to submit to Dev Center, right- click on your project and select **Store > Create App Packages**.
8. Validate your app package locally by running Windows Certification Kit.

> [!NOTE] 
> Make sure you validate your app package locally with the Windows Certification Kit. For more information about testing your app with the Windows App Certification Kit, see [Windows App Certification Kit](https://msdn.microsoft.com/library/windows/apps/mt186449).

### Submit an app with Dev Center

1. Now submit the app package in Dev Center, as explained in [App submissions](https://msdn.microsoft.com/en-us/windows/uwp/publish/app-submissions).
2. During submission, select the option to hide your application and prevent acquisition.

![Hide your application option in Windows Dev Center](BUGBUG NEED IMAGE)

3. The values are set in the app submission – store listing step. For each language you want to support, you will need a separate store listing with localized strings. See [create app Store listings](https://docs.microsoft.com/en-us/windows/uwp/publish/create-app-store-listings).

![Window Dev Center App submission, App description page](BUGBUG NEED IMAGE)

![Window Dev Center App submission, App description page](BUGBUG NEED IMAGE)

4. Place the following text in [Notes for certification](https://msdn.microsoft.com/en-us/windows/uwp/publish/notes-for-certification) when submitting your app in Windows Dev Center: &quot;Please escalate any possible policy issues to [acoexp@microsoft.com](mailto:acoexp@microsoft.com) or [datamartpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com). This app is being published to enable this Dev Center account to publish Connectivity Offer In-App-Purchases that are discoverable in Microsoft&#39;s Data Marketplace pre-installed Windows app. The app currently being published is marked as hidden because it&#39;s not intended for retail customer consumption. Microsoft&#39;s Data Marketplace helps Windows customers discover, purchase and connect to wireless connectivity that&#39;s sold in Windows Store.  Feel free to contact the Data Marketplace team at [datamartpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com).
5. Submit your app. It typically takes one or two days to receive the certification result. Proceed to next step after receiving an app was certified email from Windows Dev Center.

> [!NOTE]
> If your app fails certification, reach out to [datamartpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com).


## Configure your Dev Center account for Data Marketplace

After the app has been certified there are a few additional steps to perform before this first phase is complete.

### Add Microsoft&#39;s Data Marketplace Client ID to your app.

This allows Microsoft&#39;s Data Marketplace service to sell your connectivity offers.

1. Log into Dev Center, select your app in the Dashboard, select **Services** in the left-hand menu and then navigate to **Product collections and purchases** _._ In the _Client ID 1_ field copy/paste this text: **7b02d2d1-f9cd-497c-8064-bac0d8711e97**.

![Windows Dev Center Product Collection Page](BUGBUG NEED IMAGE)

## Email Data Marketplace integration details

Send an email to [datamartpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com) with the following information for Windows Store PAYG onboarding:

1. The brand name you want to use for your products. It is a universal brand name across all your apps.
2. Mutual TLS authentication (MTLS). You can also provide basic authentication if you want in the initial integration phase, but MTLS is required before completing the integration work. We need this information for MTLS validation.
3. For each app you own, provide the information by filling in:
  - Dev Center App ID.
  - SIM ICC ID ranges that you want to associate with each App you own.
  - Supported location for offer discovery for each App you own. Note that one App can have multiple offers with each offer available in different locations. For a particular App, the &quot;Supported Location&quot; should be a union of all locations supported by all offers published in this App.
  - Provider service URI for each App you own. This is required for end-to-end testing. This is also referred to as &quot;moBaseUrl&quot;.

Here is an example:

| App ID | SIM ICC ID Range | Supported Location | Provider Service URI |
| --- | --- | --- | --- |
| 9N08DS9T6W40 | 894230600002575694-894230600002775693; 894236000024748200-894236000024748299; | US; FR; | https<span></span>://service.contoso.com |
| 9NBLGGH42M6H | 894230600002575600-894230600002775699 | BR | https<span></span>://service.contoso.com/v1 |

Send an email to [datamartpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com) with the following information for MO Direct onboarding:

1. List of countries that MO Direct is supported
2. MO Direct portal URI
3. The notification URI 

## Add &amp; publish connectivity offers

After we have granted permission you are free to add connectivity offers. Go to Dev Center and follow this tutorial to publish an [add-on](https://msdn.microsoft.com/en-us/windows/uwp/publish/iap-submissions) (IAP/in-app-product).  Note that your connectivity offers will not be available to customers through the Paid Wi-Fi &amp; Cellular app until after we publish them at the end of the development cycle.

Keep these points in mind:

1. Currently, providers can only create non-recurring offers by setting the **product type** to &quot;Developer-managed consumable&quot;. A customer that purchases 200 MB of cellular data that expires after 24 hours is charged once, and when 24 hours passes or the 200 MB is consumed, the customer is no longer entitled to connectivity until they purchase another offer.

![Product type for connectivity offers](BUGBUG NEED IMAGE)

2. After selecting the product type, set the **content type** to &quot;Connectivity offer&quot;.

![Content type for connectivity offers](BUGBUG NEED IMAGE)

3. Enter Data Marketplace and connectivity offer specific information in the **Tag** textbox (3000 character limit). This information must be formatted in JSON, which resembles the following format.  This must be repeated for each IAP.  The table below explains how each field is used.

| JSON key | Example Value(s) | Description |
|:--- |:--- |:--- |
| microsoftDataVersion | 2 | This allows us to evolve the schema without breaking past offers. |
| microsoftData | N/A | This object tells Data Marketplace where to expose the offer. |
| offerType | Normal Test | This field is case sensitive. This informs Data Marketplace it is a public offer (Normal) or that the offer is for internal testing (Test) and thus hidden from customers. |
| location | US  | This dictates the physical location (country) the customer must be located to see the offer. If it&#39;s only a single country, use the key and format in this row. If it&#39;s a list of countries, use the key and format in the next row. This is different than the availabilities (market) you&#39;ll set up for the IAP, which is used to present an offer in a customer&#39;s currency and language / locale.   [ISO 3166-1 alpha-2 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |
| locations | [US, GB, FR] | A list of countries (no more than 60) where the customer must be located to see the offer. |
| providerData  | &quot;providerData&quot;:&quot;{ \&quot;Version\&quot;:\&quot;2\&quot;, \&quot;Data\&quot;:\&quot;{ \\\&quot;location\\\&quot;:\\\&quot;US\\\&quot;, \\\&quot;isMicrobalance\\\&quot;:\\\&quot;true\\\&quot;, \\\&quot;productId\\\&quot;:\\\&quot;CXZV7MW0H0XN\\\&quot;, \\\&quot;dataQuantaInMB\\\&quot;:3, \\\&quot;timeQuanta\\\&quot;:\\\&quot;00:00:01:00\\\&quot;}\&quot;}&quot;}   | This data is passed to you when Data Marketplace calls into your system to provision network access. It is transparent to Data Marketplace services and you may put any data you desire, as long as it&#39;s valid JSON and follow the same escaping rules as in the example on the left.Examples of data that may be placed here include: expiry of the data purchased or the amount of data that must be provisioned as a result of purchasing the offer. Note, this data is made available only after you have begun network integration with Microsoft. |

![Connectivity offer properties](BUGBUG NEED IMAGE)

4. [Set Pricing and Availability](https://msdn.microsoft.com/en-us/windows/uwp/publish/set-add-on-pricing-and-availability) for available markets. A customer&#39;s market is determined by the region setting in Windows Settings -&gt; Time &amp; Language -&gt; Country or region.
5. [Create Store Listings](https://msdn.microsoft.com/en-us/windows/uwp/publish/create-add-on-store-listings) for every language you want to support. The values are set in Add-on Store Listings. Icon for add-on is optional and it will be displayed in the order confirmation email customer receives after purchase. Add-on icon is not displayed in Paid Wi-Fi &amp; Cellular App.

![Store listing for connectivity offer](BUGBUG NEED IMAGE)

> [!NOTE] 
> For Windows Store market availability and tax remittance be sure to review [Tax details for paid apps](https://msdn.microsoft.com/en-us/windows/uwp/publish/tax-details-for-paid-apps) (and IAPs), it explains where the Store remits taxes and where you&#39;re expected to remit taxes.

### Retrieve your offer ID

Offer ID will be useful for debugging and reporting purposes. You can find your offer ID on the offer submission page:

![Retrieve your offer ID](BUGBUG NEED IMAGE)

This page&#39;s URL also has the offer ID: https://developer.microsoft.com/en-us/dashboard/iaps/9NBLGGH5108R?appId=9NBLGGH4NXJ7

### Connectivity offer regional coverage

There are three notions of &quot;location&quot; when it comes to a connectivity offer:

1. Windows Store market availability. These offer listing settings determines in what price, currency and language the customer will see your offer. A customer&#39;s market is determined by the region setting in Windows Settings -&gt; Time &amp; Language -&gt; Country or region.
2. Location in &quot;microsoftData&quot;. This location attribute determines where the customer needs to be physically to see the offer. Note that we only support a single value for this attribute currently.
3. Location information defined by provider which determines where the offer can be consumed.

Here are some examples for connectivity offers with different regional coverage:

| Offer # | Value for store listing market(s) | Value for &quot;location&quot; in &quot;microsoftData&quot; for plan purchasing (max 20 countries)   | Location information defined by provider for plan consumption   | Description |
| --- | --- | --- | --- | --- |
| 1 | US | US | US | Domestic offer that can only be purchased and consumed in US |
| 2 | US | US | US, FR | International offer that can be purchased in US and consumed in both US and FR |
| 3 | US, GB, FR | US, GB, FR | US, GB, FR | Regional offers that cover US, GB and FR. |

### Supported connectivity offer types

Currently, only pay-as-you-go (PAYG) plans are supported through Windows Store and Windows Dev Center. These are connectivity offers with pre-determined duration and data limit, such as 250MB data, expires in 24 hours.

Recurring billing on prepaid plans is not supported through Windows Store.

Stacking multiple Windows Store PAYG offers is not supported either.

### Manage connectivity offers with bulk update

You can [manage connectivity offers in bulk](https://docs.microsoft.com/en-us/windows/uwp/publish/manage-add-ons-in-bulk). Note that &quot;ConnectivityOffer&quot; content type is only supported in Excel mode.

### Submit connectivity offers with Windows Store Submission API

You can also [submit offers through Windows Store Submission API](https://docs.microsoft.com/en-us/windows/uwp/monetize/create-and-manage-submissions-using-windows-store-services). This section explains how to use StoreBroker to submit connectivity offers step-by-step.

1. Install StoreBroker using the [instructions provided here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/SETUP.md#installation). You&#39;ll need to complete all of the steps under the Installation section.
2. Validate that you have met all of the [prerequisites listed here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/SETUP.md#prerequisites), and then follow the [instructions for setting up authentication](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/SETUP.md#authentication).
3. You will need your app ID to continue. If you don&#39;t already know the ID, you can either get it from Dev Center, or you can get it using the [steps listed here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/SETUP.md#getting-your-appid).

4. You will also need the ID of an offer that has already been submitted and validated to work with Data Marketplace. (It doesn&#39;t matter which offer you use, as long as you use a valid one.) You can either get the ID from Dev Center, or using the [steps listed here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/SETUP.md#getting-your-iapid). To get your IAP ID from Dev Center:
  1. Go to your Dev Center dashboard, then browse to your app&#39;s page.
  2. Under the &quot;Add-ons&quot; section, select your offer.
  3. The ID is listed directly under the IAP title as &quot;Store ID&quot;.
5. Clone your existing offer&#39;s PDP files [using these instructions](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/SETUP.md#getting-your-iap-pdps). These will serve as a base for the offer that you will be submitting using this tool. A few notes:
  1. The &quot;ConvertFrom-ExistingIapSubmission.ps1&quot; script mentioned in the instructions is located in the StoreBroker installation directory. You can either run the command from the installation directory, or replace the period with the installation directory. If you followed the suggestion in the installation instructions, the installation directory should be &quot;C:\Customers\&lt;username&gt;\Documents\WindowsPowerShell\Modules\StoreBroker&quot;
  2. The value you use for &quot;Release&quot; does not matter unless you plan to upload screenshots. The Paid Wi-Fi &amp; Cellular app does not use IAP screenshots, so you do not need to upload them unless you want an image to appear in the email receipts sent to your customers.
  3. You must provide the full filepath for OutPath. For example:
    a. &quot;C:\Customers\&lt;username&gt;\Documents\OfferUpload\PDP&quot;
  4. This script will create a file for every language uploaded for the offer you selected in step 4. For example, if you choose an offer that has descriptions in English and French, then the files created in this step will be for English and French.
6. Obtain a config file for your IAP [using the instructions here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/SETUP.md#getting-your-iap-config). You will modify this file to create your new offer.
7. Run the New-InAppProduct command as [explained here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/USAGE.md#creating-andor-removing-iaps) in order to create an ID for your new offer. You will need this ID in the next step. Two notes:
  a. Set &quot;ProductType&quot; to &quot;Consumable&quot;. **This is very important.**
  b. Set &quot;ApplicationIds&quot; to the ID you got from step 3. You do not need multiple IDs.
8. Open the config file you created in the previous step and modify it as follows (some of these are also listed [here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/SETUP.md#config-setup-steps)):
  a. Set all the fields in &quot;packageParameters&quot; according to the comments in the file. Note that you can also pass any of these in the command-line at a later time, if you&#39;d rather not save them in this file right now.
  a. Under &quot;iapSubmission&quot;, set the following fields:
    - Set &quot;iapId&quot; to the output from step 7.
    - Make sure that &quot;contentType&quot; is set to &quot;ConnectivityOffer&quot;.
    - The &quot;tag&quot; field contains your Data Marketplace offer data. Modify all of the offer data fields as needed to match the new offer you want to submit. Note that this field has been XML-escaped further than the one in Dev Center. If you need to add or remove special characters (such as quotation marks), pay close attention to the number of backslashes you use.
  3. Under &quot;pricing&quot;, set the priceId and marketSpecificPricings as desired. The price tiers are not linked to in the config file, but can be viewed in Dev Center. To find the price tiers:
    a. Go to your app&#39;s Dev Center page and select an existing offer.
    b. Select a submission. Any submission is fine.
    c. Select &quot;Pricing and Availability&quot;.
    d. Under &quot;Markets and custom prices&quot;, select &quot;view table&quot;.
    e. Select the Tier you want based on the prices in the table. Be sure to format the field as &quot;TierX&quot;, where X is the tier number from the table.
9. Go to the folder where your PDP files are (the folder you specified in step 5). Open each language subdirectory and modify the PDP file. Change the title and description to match the new offer you want to submit. **You must do this for each language file.**
10. [Follow the instructions here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/USAGE.md#creating-your-iap-payload) to generate the payload for your new offer. A few notes:
  a. Any fields that you did not set in step 8a must be specified as part of the New-InAppProductSubmissionPackage command.
  b. The directory you specify for OutPath must exist before you run the command. Running this command will not create a new directory for you.
11. Publish your new offer using the Update-InAppProductSubmission command [as explained here](https://github.com/Microsoft/StoreBroker/blob/master/Documentation/USAGE.md#iap-commands). Note: &quot;PackagePath&quot; must be the full file path for the ZIP file generated in step 10.
12. Your offer will now go through the certification and publishing steps as usual. If you&#39;d like to monitor its progress, check the output from step 11 for a command (Start-InAppProductSubmissionMonitor) you can run to start a monitor and receive email notifications.

## Make offers unavailable

For audit and legal reasons, you cannot delete an add-on in Windows Store once submitted. To make an offer not available for Data Marketplace / Windows Store customers, update the offer Pricing and Availability.

![Make an offer unavailable for purchase](BUGBUG NEED IMAGE)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
