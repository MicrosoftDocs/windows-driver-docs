---
title: Mobile Plans promotional content
description: Mobile Plans promotional content
ms.assetid: FB789462-732C-436A-B69C-43940F7F8A77
keywords:
- Windows Mobile Plans promotional content mobile operators
ms.author: windowsdriverdev
ms.date: 09/28/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mobile Plans promotional content

[!include[Mobile Plans Beta Prerelease](../mobile-plans-beta-prerelease.md)]

## Overview

This topic provides instructions for mobile operators to create and submit promotional campaign content in the Mobile Plans app.

## Promotional notifications

Windows includes support for interactive toast notifications that include text, images and button inputs. The Mobile Plans app enables mobile operators to show promotional content in toast notifications that can be triggered by the app.

## Promotional gateways

The Mobile Plans app includes a landing page for every mobile operator. The landing page can be customized with promotional content to highlight a brand or campaign message.

Promotional gateway content is defined using a JSON file with the following elements:

```JSON
{ // Root object
  "promotionTemplates": [
    { // PromotionTemplate
      "id": 123,
      "backgroundColor": "0x000000FF", // Black
      "bodyFontColor": "0xFFFFFFFF", // White
      "buttonColor": "0x414243FF", // Grey
      "buttonFontColor": "0xFFFFFFFF", // White
      "bodyText": "We’ll help you find a plan so you can get connected when W-Fi isn’t available",
      "buttonText": "Get started",
      "images": [
        { // Image
          "height": 480,
          "uri": "https://storagetos.datamart.windows.com/MO1/v1/en-US/landing740x480.png",
          "width": 740,
        }
      ]
    }
  ]
}
```

The following table describes each JSON object in the previous example.

| JSON object | Field name | Description | Example |
| --- | --- | --- | --- |
| Root object | promotionTemplates | A list of promotion templates to be shown on the gateway page. Only one promotion template is supported for each mobile operator. | N/A |
| PromotionTemplate | id | A unique string identifier for the template. | 123 |
|   | backgroundColor | The background color of the gateway page. This field is a hexadecimal string in the format of `0xRRGGBBAA`. If undefined, white is used as the default. | 0x000000FF |
|   | bodyFontColor | The font color for the body text. This field is a hexadecimal string in the format of `0xRRGGBBAA`. If undefined black is used as the default. | 0xFFFFFFFF |
|   | buttonColor | The color of the "Continue" button that launches the mobile operator's portal. This field is a hexadecimal string in the format of `0xRRGGBBAA`. If undefined, the user-selected system highlight color is used as the default. | 0x414243FF |
|   | buttonFontColor | The font color for the text on the "Continue" button. This field is a hexadecimal string in the format of `0xRRGGBBAA`. If undefined, white is used as the default. | 0xFFFFFFFF | 
|   | bodyText | The localized body text for the client's language. | We'll help you find a plan so you can get connected when Wi-Fi isn't available. |
|   | buttonText | The localized text for the "Continue" button. | Get started |
|   | images | Images to use for the template. Different sizes are supported. If multiple sizes are included, the Mobile Plans app uses the optimum size for the screen resolution. | ![Mobile plans Surface landing page example, 780x480](images/mobile_plans_surface_landing_780x480.png) |

### Example promotional gateway landing page

![Example promotional gateway landing page in the Mobile Plans app](images/mobile_plans_sample_landing_page.png)