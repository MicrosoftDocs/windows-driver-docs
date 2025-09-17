---
title: Request device identifiers for eSIM provisioning
description: Mobile operators can request device-specific information such as IMEI, EID, and ICCID through a user-consented dialog in Windows Settings
ms.date: 09/17/2025
ms.topic: best-practice
---

# Request device identifiers for eSIM provisioning

Mobile operators may require device identifiers to provision an eSIM profile for users. On Windows devices, these identifiers can be accessed through the Cellular Identifiers dialog. The Cellular Device Identifiers feature enables mobile operators to request device-specific information — such as IMEI (International Mobile Equipment Identity), EID (Embedded Identity Document), MAKE, and MODEL — via a user-consented dialog in Windows Settings.

## What is the *ms-settings:cellular-id* protocol?

The `ms-settings:cellular-id` protocol is a Windows protocol link that launches the Cellular Device Identifiers dialog in Windows Settings. This protocol enables mobile operators to request device-specific information with user consent.

## Supported identifiers

The following identifiers are supported:

- **IMEI** - Identifier of the cellular device
- **EID** - Identifier of the eSIM module  
- **ICCID** - Identifier of the active SIM, if there is one
- **Make** - Make of the device (base64 encoded)
- **Model** - Model of the device (base64 encoded)

## How to request identifiers

Device identifiers can be requested in two ways:

### Method 1: Request identifiers via a callback URL

Mobile operators can provide a callback URL that includes placeholders for the required device identifiers. This callback URL enables automatic population of the identifiers when the user consents to share them. The callback URL with the populated identifiers is launched in the default web browser.

The callback URL must be a valid URL utilizing the HTTPS protocol. It should be appended to the Windows protocol in the following format:

```
ms-settings:cellular-id?callbackUrl=<callbackURL>
```

The callback URL should have at least one of the supported identifier placeholders:

```
https://contoso.com/?eid={eid}&make={make}&model={model}&iccid={iccid}&imei={imei}
```

Example JavaScript code:

```javascript
function launchCellularIdentifiers() {
    var protocol = "ms-settings:cellular-id?callbackurl=https://contoso.com/?eid={eid}&make={Make}&model={model}&iccid={iccid}&imei={imei}";
    
    window.location.href = protocol;
    
    console.log("launching protocol: " + protocol);
}
```

After user consent, the callback URL with filled identifiers would be:
```
https://contoso.com/?eid=12345678&make=VGVzdE1ha2U=&model=VGVzdE1vZGVs&iccid=012345678&imei=234567898
```

**Note:** Make and model values are encoded using base64 format.

### Method 2: Display identifiers directly to the user

Mobile operators can invoke the Windows protocol `ms-settings:cellular-id` from their web portal without a callback URL. This protocol opens a dialog in Windows Settings that displays key device identifiers, allowing users to manually copy and paste them into the operator's portal.

Example JavaScript code:

```javascript
function launchCellularIdentifiers() {
    var protocol = "ms-settings:cellular-id"; 
    window.location.href = protocol;
    
    console.log("launching protocol: " + protocol);
}
```

## What does the user see?

When the protocol is invoked, Windows displays a consent dialog asking the user to share device identifiers. Depending on the method used:

- **With callback URL**: After consent, the browser automatically navigates to the callback URL with populated identifiers
- **Without callback URL**: A dialog displays the identifiers for manual copying

The specific identifiers shown depend on the device configuration and may include IMEI, EID, and ICCID.

## Troubleshooting

The following error dialogs may appear:

### Selected SIM slot doesn't support eSIM
This dialog appears when the callback URL requests the EID but the device is currently using a physical SIM slot or doesn't support eSIM.

### Unexpected issue dialog
This dialog may appear if there's an issue with the callback URL:
- The callback URL doesn't begin with the HTTPS protocol
- The callback URL is invalid  
- The callback URL doesn't include at least one supported identifier

## Best practices

Microsoft recommends that mobile operators:
- Use HTTPS protocol for all callback URLs
- Include appropriate error handling for unsupported devices
- Provide clear instructions to users when manual identifier entry is required
- Test the implementation across different device types and configurations

## Related content

[Use a QR code or URI link to download an eSIM profile](activate-by-link.md)