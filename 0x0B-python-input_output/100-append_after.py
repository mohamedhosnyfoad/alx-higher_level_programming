{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x0B-python-input_output":{"items":[{"name":"0-read_file.py","path":"0x0B-python-input_output/0-read_file.py","contentType":"file"},{"name":"1-write_file.py","path":"0x0B-python-input_output/1-write_file.py","contentType":"file"},{"name":"10-student.py","path":"0x0B-python-input_output/10-student.py","contentType":"file"},{"name":"100-append_after.py","path":"0x0B-python-input_output/100-append_after.py","contentType":"file"},{"name":"101-stats.py","path":"0x0B-python-input_output/101-stats.py","contentType":"file"},{"name":"11-student.py","path":"0x0B-python-input_output/11-student.py","contentType":"file"},{"name":"12-pascal_triangle.py","path":"0x0B-python-input_output/12-pascal_triangle.py","contentType":"file"},{"name":"2-append_write.py","path":"0x0B-python-input_output/2-append_write.py","contentType":"file"},{"name":"3-to_json_string.py","path":"0x0B-python-input_output/3-to_json_string.py","contentType":"file"},{"name":"4-from_json_string.py","path":"0x0B-python-input_output/4-from_json_string.py","contentType":"file"},{"name":"5-save_to_json_file.py","path":"0x0B-python-input_output/5-save_to_json_file.py","contentType":"file"},{"name":"6-load_from_json_file.py","path":"0x0B-python-input_output/6-load_from_json_file.py","contentType":"file"},{"name":"7-add_item.py","path":"0x0B-python-input_output/7-add_item.py","contentType":"file"},{"name":"8-class_to_json.py","path":"0x0B-python-input_output/8-class_to_json.py","contentType":"file"},{"name":"9-student.py","path":"0x0B-python-input_output/9-student.py","contentType":"file"},{"name":"README.md","path":"0x0B-python-input_output/README.md","contentType":"file"}],"totalCount":16},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x08-python-more_classes","path":"0x08-python-more_classes","contentType":"directory"},{"name":"0x09-python-everything_is_object","path":"0x09-python-everything_is_object","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0B-python-input_output","path":"0x0B-python-input_output","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":14}},"fileTreeProcessingTime":3.9851469999999996,"foldersToFetch":[],"repo":{"id":677116802,"defaultBranch":"master","name":"alx-higher_level_programming","ownerLogin":"eslamalawy","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2023-08-10T19:26:14.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/125456763?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1707368432.0","canEdit":false,"refType":"branch","currentOid":"7210815463a9975bab9515baa3cea90bced4f4f1"},"path":"0x0B-python-input_output/100-append_after.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"Contains the \"append after\" function\"\"\"","","","def append_after(filename=\"\", search_string=\"\", new_string=\"\"):","    \"\"\"appends \"new_string\" after a line containing","    \"search_string\" in \"filename\" \"\"\"","    with open(filename, 'r', encoding='utf-8') as f:","        line_list = []","        while True:","            line = f.readline()","            if line == \"\":","                break","            line_list.append(line)","            if search_string in line:","                line_list.append(new_string)","    with open(filename, 'w', encoding='utf-8') as f:","        f.writelines(line_list)"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":42,"cssClass":"pl-s"}],[],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":16,"cssClass":"pl-en"},{"start":17,"end":25,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-c1"},{"start":26,"end":28,"cssClass":"pl-s"},{"start":30,"end":43,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":44,"end":46,"cssClass":"pl-s"},{"start":48,"end":58,"cssClass":"pl-s1"},{"start":58,"end":59,"cssClass":"pl-c1"},{"start":59,"end":61,"cssClass":"pl-s"}],[{"start":4,"end":51,"cssClass":"pl-s"}],[{"start":0,"end":37,"cssClass":"pl-s"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":22,"cssClass":"pl-s1"},{"start":24,"end":27,"cssClass":"pl-s"},{"start":29,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":45,"cssClass":"pl-s"},{"start":47,"end":49,"cssClass":"pl-k"},{"start":50,"end":51,"cssClass":"pl-s1"}],[{"start":8,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"}],[{"start":8,"end":13,"cssClass":"pl-k"},{"start":14,"end":18,"cssClass":"pl-c1"}],[{"start":12,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":29,"cssClass":"pl-en"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":22,"cssClass":"pl-c1"},{"start":23,"end":25,"cssClass":"pl-s"}],[{"start":16,"end":21,"cssClass":"pl-k"}],[{"start":12,"end":21,"cssClass":"pl-s1"},{"start":22,"end":28,"cssClass":"pl-en"},{"start":29,"end":33,"cssClass":"pl-s1"}],[{"start":12,"end":14,"cssClass":"pl-k"},{"start":15,"end":28,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-c1"},{"start":32,"end":36,"cssClass":"pl-s1"}],[{"start":16,"end":25,"cssClass":"pl-s1"},{"start":26,"end":32,"cssClass":"pl-en"},{"start":33,"end":43,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-k"},{"start":9,"end":13,"cssClass":"pl-en"},{"start":14,"end":22,"cssClass":"pl-s1"},{"start":24,"end":27,"cssClass":"pl-s"},{"start":29,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":38,"end":45,"cssClass":"pl-s"},{"start":47,"end":49,"cssClass":"pl-k"},{"start":50,"end":51,"cssClass":"pl-s1"}],[{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":20,"cssClass":"pl-en"},{"start":21,"end":30,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/eslamalawy/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null},"displayName":"100-append_after.py","displayUrl":"https://github.com/eslamalawy/alx-higher_level_programming/blob/master/0x0B-python-input_output/100-append_after.py?raw=true","headerInfo":{"blobSize":"598 Bytes","deleteTooltip":"You must be signed in to make or propose changes","editTooltip":"You must be signed in to make or propose changes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","isGitLfs":false,"gitLfsPath":null,"onBranch":true,"shortPath":"92df673","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Feslamalawy%2Falx-higher_level_programming%2Fblob%2Fmaster%2F0x0B-python-input_output%2F100-append_after.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"18","truncatedSloc":"16"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/eslamalawy/alx-higher_level_programming/blob/master/0x0B-python-input_output/100-append_after.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/eslamalawy/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/eslamalawy/alx-higher_level_programming/raw/master/0x0B-python-input_output/100-append_after.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"eslamalawy","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"append_after","kind":"function","ident_start":68,"ident_end":80,"extent_start":64,"extent_end":597,"fully_qualified_name":"append_after","ident_utf16":{"start":{"line_number":4,"utf16_col":4},"end":{"line_number":4,"utf16_col":16}},"extent_utf16":{"start":{"line_number":4,"utf16_col":0},"end":{"line_number":17,"utf16_col":31}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/eslamalawy/alx-higher_level_programming/branches":{"post":"0igFlxjNs_jxAoFQUsTmbQGf4BBrj5-4KSoQWN3m7eLRoB62ac5djxazX2Tf_2pqJiavUkmr1gAGsRt73jpk0A"},"/repos/preferences":{"post":"oV1Xg_4kGfYrzN1hDNVz0fxz4tA3dRgq9x-tx17LwbNOE7rlEe_0i5gp3wdYhMYNJSbrjTNPuyNH8ZuTuvZTdg"}}},"title":"alx-higher_level_programming/0x0B-python-input_output/100-append_after.py at master · eslamalawy/alx-higher_level_programming"}