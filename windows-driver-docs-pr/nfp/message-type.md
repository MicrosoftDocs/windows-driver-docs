---
title: Message Type
description: Message Type
ms.assetid: 3C64F85F-D8AE-4448-A75C-965DCCD85216
---

# Message Type


The message type is a dot-delimited null-terminated string that defines the contents, meaning, and intended consumers of the message. An example is:

``` syntax
    Windows.contoso.com:t
```

The message type must always begin with a protocol component and can be followed by more specific subtype information. From the perspective of NFP providers, only the protocol component needs to be parsed out and evaluated by the provider. The rest can be opaque and need only be used for matching published messages with subscribers.

## Protocol Component


The protocol component of the message type is defined as everything before the first dot in the message type, or the entire string if it contains no dots. As an example, the highlighted portion of **Windows**`.contoso.com:t` shows the protocol component.

The protocol component is a standardized unique string that defines the primary level of branching for provider message handling. The string is case-sensitive. The parameter indicates to the NFP provider what the contents of *messageData* are as well as what protocol to use when transmitting the message.

A message intended to be transmitted or received over NFC would use the “NDEF” protocol and *messageData* should be assumed to already be formatted according to a specific NDEF standard.

All NFP providers are required to support the “Windows” protocol. When “Windows” is specified, *messageData* is formatted so that Windows can decode and understand the message. However, *messageData* is not encoded to any NFP technology standards. The NFP provider will need to wrap the message parameters in the appropriate protocol headers so that it can be transmitted to a receiver on a Windows device.

The protocol component corresponds to standardized types that the NFP provider understands and supports. An NFP provider must return an error when the caller specifies a protocol that the driver is not expecting. This avoids confusion among callers about why a message is not encoded to the expected protocol.

The maximum length of the Protocol component is 250 characters (not including the dot or NULL terminator).

## Subtype Component


The subtype component of *messageType* is defined as everything after the first dot. As an example, the highlighted portion of `Windows`**.contoso.com:t** shows the subtype component.

The subtype component may be defined by Windows or by apps. The NFP provider should use it to deliver messages only to subscribers of the specified *messageType*.

The subtype string is case-sensitive and describes the contents of the message.

Providers MUST, at a minimum, support the following characters; for published types, limiting use to the following characters is RECOMMENDED:

-   Alphanumeric:

    `[A-Za-z0-9]`

-   Plus the following non-alphanumeric characters:

    `- . _~ : / ? # [ ] @ ! $ & ‘ ( ) * + , ; = %`

For the “Windows” protocol, the subtype string should follow the URI naming scheme. This allows two different implementers to create types independently while ensuring that they don’t accidentally end up using the same type.

The maximum length of the subtype component is 250 characters (not including the NULL terminator). However, shorter type names are RECOMMENDED due to the short-message nature of typical proximity technologies.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Message%20Type%20%20RELEASE:%20%283/30/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




