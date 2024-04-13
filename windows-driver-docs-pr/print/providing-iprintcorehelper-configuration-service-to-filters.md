---
title: Providing IPrintCoreHelper Configuration Service to Filters
description: Providing IPrintCoreHelper Configuration Service to Filters
ms.date: 01/30/2023
---

# Providing IPrintCoreHelper Configuration Service to Filters

[!include[Print Support Apps](../includes/print-support-apps.md)]

The **IPrintCoreHelper** interface is a new interface that is implemented by the Windows Vista Unidrv/PScript5 configuration module. This interface allows the client machine to:

1. Enumerate GPD or PPD features, options, and constraints.

1. Get values for PPD's global, feature, or option attributes.

1. Get current settings for doc-sticky and printer-sticky GPD or PPD features.

1. Create a GDL parser snapshot for full access to GPD and GDL content.
