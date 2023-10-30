---
title: IPrinterBidiSchemaResponses interface
description: The IPrinterBidiSchemaResponses interface represents a set of bidi responses populated by USB Bidi Extension JavaScript methods getSchemas and getStatus.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
keywords: ["IPrinterBidiSchemaResponses interface Print Devices", "IPrinterBidiSchemaResponses interface Print Devices , described"]
topic_type:
- apiref
ms.topic: reference
api_name:
- IPrinterBidiSchemaResponses
api_type:
- COM
ms.date: 07/13/2023
---

# IPrinterBidiSchemaResponses interface

The IPrinterBidiSchemaResponses interface represents a set of bidi responses populated by USB Bidi Extension JavaScript methods **getSchemas** and **getStatus**.

## Members

The **IPrinterBidiSchemaResponses** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IPrinterBidiSchemaResponses** also has these types of members:

- [Methods](#methods)

### Methods

The **IPrinterBidiSchemaResponses** interface has these methods:

| Method | Description |
|--|--|
| [**AddBool**](iprinterbidischemaresponses--addbool.md) | The AddBool method adds a new response of type BIDI_BOOL to the collection. |
| [**AddInt32**](iprinterbidischemaresponses--addint32.md) | The AddInt32 method adds a new response of type BIDI_INT to the collection. |
| [**AddBlob**](iprinterbidischemaresponses-addblob.md) | The AddBlob method adds a new response of type BIDI_BLOB to the collection. |
| [**AddEnum**](iprinterbidischemaresponses-addenum.md) | The AddEnum method adds a new response of type BIDI_ENUM to the collection. |
| [**AddFloat**](iprinterbidischemaresponses-addfloat.md) | The AddFloat method adds a new response of type BIDI_FLOAT to the collection. |
| [**AddNull**](iprinterbidischemaresponses-addnull.md) | The AddNull method adds a new response of type BIDI_NULL to the collection. |
| [**AddRequeryKey**](iprinterbidischemaresponses-addrequerykey.md) | The AddRequeryKey method adds a new QueryKey to re-query upon return from the getSchemas call. |
| [**AddString**](iprinterbidischemaresponses-addstring.md) | The AddString method adds a new response of type BIDI_STRING to the collection. |
| [**AddText**](iprinterbidischemaresponses-addtext.md) | The AddText method adds a new response of type BIDI_TEXT to the collection. |
