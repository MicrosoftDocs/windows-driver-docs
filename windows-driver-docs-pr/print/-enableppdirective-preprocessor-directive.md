---
title: '#EnablePPDirective Preprocessor Directive'
description: '#EnablePPDirective Preprocessor Directive'
ms.assetid: aebb11ec-b281-461e-b3fd-65e9b2773049
keywords:
- preprocessor directives WDK GDL , keywords
- keywords WDK GDL
- reserved keywords WDK
- EnablePPDirective directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \#EnablePPDirective Preprocessor Directive


```GDL
#EnablePPDirective: Directive
```

The \#EnablePPDirective allows disabled directives to be enabled. Future versions of the GDL parser might define additional preprocessor directives. If existing GDL files have also used that new directive name for their own purposes, parsing the existing GDL file could have unexpected results on the new parser. To avoid this forward-compatibility problem, any new directives will be disabled by default and will need to be enabled by using the \#EnablePPDirective directive. The *Directive* value is the base name of the directive to be enabled (without any prefix). The directive name is a required value.

This preprocessor directive is new for GDL.
