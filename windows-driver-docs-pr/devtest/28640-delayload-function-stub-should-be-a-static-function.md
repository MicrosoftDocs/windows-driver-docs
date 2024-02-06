---
title: C28640 Warning
description: Warning C28640 function delayload stub should be a static function.
ms.date: 04/20/2017
f1_keywords: 
  - "C28640"
---

# C28640


warning C28640: function delayload stub should be a static function

All delay-load libraries should be static; they should have no symbolic exports. This ensures that no unexpected software can link to delay-load stub functions. If this guideline is not followed, the binary potentially exposes exports that might be used inappropriately.

