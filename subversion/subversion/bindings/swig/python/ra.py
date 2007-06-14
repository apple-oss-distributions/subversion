# This file was created automatically by SWIG.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _ra

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import core
import delta

def svn_ra_version(*args):
    """svn_ra_version() -> svn_version_t"""
    return apply(_ra.svn_ra_version, args)
class svn_ra_reporter2_t:
    """Proxy of C svn_ra_reporter2_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_ra_reporter2_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_ra_reporter2_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_ra_reporter2_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["set_path"] = _ra.svn_ra_reporter2_t_set_path_set
    __swig_getmethods__["set_path"] = _ra.svn_ra_reporter2_t_set_path_get
    __swig_setmethods__["delete_path"] = _ra.svn_ra_reporter2_t_delete_path_set
    __swig_getmethods__["delete_path"] = _ra.svn_ra_reporter2_t_delete_path_get
    __swig_setmethods__["link_path"] = _ra.svn_ra_reporter2_t_link_path_set
    __swig_getmethods__["link_path"] = _ra.svn_ra_reporter2_t_link_path_get
    __swig_setmethods__["finish_report"] = _ra.svn_ra_reporter2_t_finish_report_set
    __swig_getmethods__["finish_report"] = _ra.svn_ra_reporter2_t_finish_report_get
    __swig_setmethods__["abort_report"] = _ra.svn_ra_reporter2_t_abort_report_set
    __swig_getmethods__["abort_report"] = _ra.svn_ra_reporter2_t_abort_report_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_ra_reporter2_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_ra_reporter2_t"""
        _swig_setattr(self, svn_ra_reporter2_t, 'this', apply(_ra.new_svn_ra_reporter2_t, args))
        _swig_setattr(self, svn_ra_reporter2_t, 'thisown', 1)
    def __del__(self, destroy=_ra.delete_svn_ra_reporter2_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_ra_reporter2_tPtr(svn_ra_reporter2_t):
    def __init__(self, this):
        _swig_setattr(self, svn_ra_reporter2_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_ra_reporter2_t, 'thisown', 0)
        _swig_setattr(self, svn_ra_reporter2_t,self.__class__,svn_ra_reporter2_t)
_ra.svn_ra_reporter2_t_swigregister(svn_ra_reporter2_tPtr)

class svn_ra_reporter_t:
    """Proxy of C svn_ra_reporter_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_ra_reporter_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_ra_reporter_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_ra_reporter_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["set_path"] = _ra.svn_ra_reporter_t_set_path_set
    __swig_getmethods__["set_path"] = _ra.svn_ra_reporter_t_set_path_get
    __swig_setmethods__["delete_path"] = _ra.svn_ra_reporter_t_delete_path_set
    __swig_getmethods__["delete_path"] = _ra.svn_ra_reporter_t_delete_path_get
    __swig_setmethods__["link_path"] = _ra.svn_ra_reporter_t_link_path_set
    __swig_getmethods__["link_path"] = _ra.svn_ra_reporter_t_link_path_get
    __swig_setmethods__["finish_report"] = _ra.svn_ra_reporter_t_finish_report_set
    __swig_getmethods__["finish_report"] = _ra.svn_ra_reporter_t_finish_report_get
    __swig_setmethods__["abort_report"] = _ra.svn_ra_reporter_t_abort_report_set
    __swig_getmethods__["abort_report"] = _ra.svn_ra_reporter_t_abort_report_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_ra_reporter_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_ra_reporter_t"""
        _swig_setattr(self, svn_ra_reporter_t, 'this', apply(_ra.new_svn_ra_reporter_t, args))
        _swig_setattr(self, svn_ra_reporter_t, 'thisown', 1)
    def __del__(self, destroy=_ra.delete_svn_ra_reporter_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_ra_reporter_tPtr(svn_ra_reporter_t):
    def __init__(self, this):
        _swig_setattr(self, svn_ra_reporter_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_ra_reporter_t, 'thisown', 0)
        _swig_setattr(self, svn_ra_reporter_t,self.__class__,svn_ra_reporter_t)
_ra.svn_ra_reporter_t_swigregister(svn_ra_reporter_tPtr)

class svn_ra_callbacks2_t:
    """Proxy of C svn_ra_callbacks2_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_ra_callbacks2_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_ra_callbacks2_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_ra_callbacks2_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["open_tmp_file"] = _ra.svn_ra_callbacks2_t_open_tmp_file_set
    __swig_getmethods__["open_tmp_file"] = _ra.svn_ra_callbacks2_t_open_tmp_file_get
    __swig_setmethods__["auth_baton"] = _ra.svn_ra_callbacks2_t_auth_baton_set
    __swig_getmethods__["auth_baton"] = _ra.svn_ra_callbacks2_t_auth_baton_get
    __swig_setmethods__["get_wc_prop"] = _ra.svn_ra_callbacks2_t_get_wc_prop_set
    __swig_getmethods__["get_wc_prop"] = _ra.svn_ra_callbacks2_t_get_wc_prop_get
    __swig_setmethods__["set_wc_prop"] = _ra.svn_ra_callbacks2_t_set_wc_prop_set
    __swig_getmethods__["set_wc_prop"] = _ra.svn_ra_callbacks2_t_set_wc_prop_get
    __swig_setmethods__["push_wc_prop"] = _ra.svn_ra_callbacks2_t_push_wc_prop_set
    __swig_getmethods__["push_wc_prop"] = _ra.svn_ra_callbacks2_t_push_wc_prop_get
    __swig_setmethods__["invalidate_wc_props"] = _ra.svn_ra_callbacks2_t_invalidate_wc_props_set
    __swig_getmethods__["invalidate_wc_props"] = _ra.svn_ra_callbacks2_t_invalidate_wc_props_get
    __swig_setmethods__["progress_func"] = _ra.svn_ra_callbacks2_t_progress_func_set
    __swig_getmethods__["progress_func"] = _ra.svn_ra_callbacks2_t_progress_func_get
    __swig_setmethods__["progress_baton"] = _ra.svn_ra_callbacks2_t_progress_baton_set
    __swig_getmethods__["progress_baton"] = _ra.svn_ra_callbacks2_t_progress_baton_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_ra_callbacks2_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_ra_callbacks2_t"""
        _swig_setattr(self, svn_ra_callbacks2_t, 'this', apply(_ra.new_svn_ra_callbacks2_t, args))
        _swig_setattr(self, svn_ra_callbacks2_t, 'thisown', 1)
    def __del__(self, destroy=_ra.delete_svn_ra_callbacks2_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_ra_callbacks2_tPtr(svn_ra_callbacks2_t):
    def __init__(self, this):
        _swig_setattr(self, svn_ra_callbacks2_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_ra_callbacks2_t, 'thisown', 0)
        _swig_setattr(self, svn_ra_callbacks2_t,self.__class__,svn_ra_callbacks2_t)
_ra.svn_ra_callbacks2_t_swigregister(svn_ra_callbacks2_tPtr)

class svn_ra_callbacks_t:
    """Proxy of C svn_ra_callbacks_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_ra_callbacks_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_ra_callbacks_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_ra_callbacks_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["open_tmp_file"] = _ra.svn_ra_callbacks_t_open_tmp_file_set
    __swig_getmethods__["open_tmp_file"] = _ra.svn_ra_callbacks_t_open_tmp_file_get
    __swig_setmethods__["auth_baton"] = _ra.svn_ra_callbacks_t_auth_baton_set
    __swig_getmethods__["auth_baton"] = _ra.svn_ra_callbacks_t_auth_baton_get
    __swig_setmethods__["get_wc_prop"] = _ra.svn_ra_callbacks_t_get_wc_prop_set
    __swig_getmethods__["get_wc_prop"] = _ra.svn_ra_callbacks_t_get_wc_prop_get
    __swig_setmethods__["set_wc_prop"] = _ra.svn_ra_callbacks_t_set_wc_prop_set
    __swig_getmethods__["set_wc_prop"] = _ra.svn_ra_callbacks_t_set_wc_prop_get
    __swig_setmethods__["push_wc_prop"] = _ra.svn_ra_callbacks_t_push_wc_prop_set
    __swig_getmethods__["push_wc_prop"] = _ra.svn_ra_callbacks_t_push_wc_prop_get
    __swig_setmethods__["invalidate_wc_props"] = _ra.svn_ra_callbacks_t_invalidate_wc_props_set
    __swig_getmethods__["invalidate_wc_props"] = _ra.svn_ra_callbacks_t_invalidate_wc_props_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_ra_callbacks_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_ra_callbacks_t"""
        _swig_setattr(self, svn_ra_callbacks_t, 'this', apply(_ra.new_svn_ra_callbacks_t, args))
        _swig_setattr(self, svn_ra_callbacks_t, 'thisown', 1)
    def __del__(self, destroy=_ra.delete_svn_ra_callbacks_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_ra_callbacks_tPtr(svn_ra_callbacks_t):
    def __init__(self, this):
        _swig_setattr(self, svn_ra_callbacks_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_ra_callbacks_t, 'thisown', 0)
        _swig_setattr(self, svn_ra_callbacks_t,self.__class__,svn_ra_callbacks_t)
_ra.svn_ra_callbacks_t_swigregister(svn_ra_callbacks_tPtr)


def svn_ra_initialize(*args):
    """svn_ra_initialize(apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_initialize, args)

def svn_ra_create_callbacks(*args):
    """svn_ra_create_callbacks(svn_ra_callbacks2_t callbacks, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_create_callbacks, args)

def svn_ra_open2(*args):
    """
    svn_ra_open2(svn_ra_session_t session_p, char repos_URL, svn_ra_callbacks2_t callbacks, 
        void callback_baton, 
        apr_hash_t config, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_open2, args)

def svn_ra_open(*args):
    """
    svn_ra_open(svn_ra_session_t session_p, char repos_URL, svn_ra_callbacks_t callbacks, 
        void callback_baton, apr_hash_t config, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_open, args)

def svn_ra_reparent(*args):
    """svn_ra_reparent(svn_ra_session_t ra_session, char url, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_reparent, args)

def svn_ra_get_latest_revnum(*args):
    """
    svn_ra_get_latest_revnum(svn_ra_session_t session, svn_revnum_t latest_revnum, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_latest_revnum, args)

def svn_ra_get_dated_revision(*args):
    """
    svn_ra_get_dated_revision(svn_ra_session_t session, svn_revnum_t revision, apr_time_t tm, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_dated_revision, args)

def svn_ra_change_rev_prop(*args):
    """
    svn_ra_change_rev_prop(svn_ra_session_t session, svn_revnum_t rev, char name, 
        svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_change_rev_prop, args)

def svn_ra_rev_proplist(*args):
    """
    svn_ra_rev_proplist(svn_ra_session_t session, svn_revnum_t rev, apr_hash_t props, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_rev_proplist, args)

def svn_ra_rev_prop(*args):
    """
    svn_ra_rev_prop(svn_ra_session_t session, svn_revnum_t rev, char name, 
        svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_rev_prop, args)

def svn_ra_get_commit_editor2(*args):
    """
    svn_ra_get_commit_editor2(svn_ra_session_t session, svn_delta_editor_t editor, 
        void edit_baton, char log_msg, svn_commit_callback2_t callback, 
        void callback_baton, apr_hash_t lock_tokens, 
        svn_boolean_t keep_locks, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_commit_editor2, args)

def svn_ra_get_commit_editor(*args):
    """
    svn_ra_get_commit_editor(svn_ra_session_t session, svn_delta_editor_t editor, 
        void edit_baton, char log_msg, svn_commit_callback_t callback, 
        void callback_baton, apr_hash_t lock_tokens, 
        svn_boolean_t keep_locks, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_commit_editor, args)

def svn_ra_get_file(*args):
    """
    svn_ra_get_file(svn_ra_session_t session, char path, svn_revnum_t revision, 
        svn_stream_t stream, svn_revnum_t fetched_rev, 
        apr_hash_t props, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_file, args)

def svn_ra_get_dir2(*args):
    """
    svn_ra_get_dir2(svn_ra_session_t session, apr_hash_t dirents, svn_revnum_t fetched_rev, 
        apr_hash_t props, char path, 
        svn_revnum_t revision, apr_uint32_t dirent_fields, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_dir2, args)

def svn_ra_get_dir(*args):
    """
    svn_ra_get_dir(svn_ra_session_t session, char path, svn_revnum_t revision, 
        apr_hash_t dirents, svn_revnum_t fetched_rev, 
        apr_hash_t props, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_dir, args)

def svn_ra_do_update(*args):
    """
    svn_ra_do_update(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, svn_revnum_t revision_to_update_to, 
        char update_target, svn_boolean_t recurse, 
        svn_delta_editor_t update_editor, 
        void update_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_do_update, args)

def svn_ra_do_switch(*args):
    """
    svn_ra_do_switch(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, svn_revnum_t revision_to_switch_to, 
        char switch_target, svn_boolean_t recurse, 
        char switch_url, svn_delta_editor_t switch_editor, 
        void switch_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_do_switch, args)

def svn_ra_do_status(*args):
    """
    svn_ra_do_status(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, char status_target, svn_revnum_t revision, 
        svn_boolean_t recurse, svn_delta_editor_t status_editor, 
        void status_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_do_status, args)

def svn_ra_do_diff2(*args):
    """
    svn_ra_do_diff2(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, svn_revnum_t revision, 
        char diff_target, svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t text_deltas, 
        char versus_url, svn_delta_editor_t diff_editor, 
        void diff_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_do_diff2, args)

def svn_ra_do_diff(*args):
    """
    svn_ra_do_diff(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, svn_revnum_t revision, 
        char diff_target, svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        char versus_url, 
        svn_delta_editor_t diff_editor, void diff_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_do_diff, args)

def svn_ra_get_log(*args):
    """
    svn_ra_get_log(svn_ra_session_t session, apr_array_header_t paths, 
        svn_revnum_t start, svn_revnum_t end, int limit, 
        svn_boolean_t discover_changed_paths, svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_log, args)

def svn_ra_check_path(*args):
    """
    svn_ra_check_path(svn_ra_session_t session, char path, svn_revnum_t revision, 
        svn_node_kind_t kind, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_check_path, args)

def svn_ra_stat(*args):
    """
    svn_ra_stat(svn_ra_session_t session, char path, svn_revnum_t revision, 
        svn_dirent_t dirent, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_stat, args)

def svn_ra_get_uuid(*args):
    """svn_ra_get_uuid(svn_ra_session_t session, char uuid, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_get_uuid, args)

def svn_ra_get_repos_root(*args):
    """svn_ra_get_repos_root(svn_ra_session_t session, char url, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_get_repos_root, args)

def svn_ra_get_locations(*args):
    """
    svn_ra_get_locations(svn_ra_session_t session, apr_hash_t locations, char path, 
        svn_revnum_t peg_revision, apr_array_header_t location_revisions, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_locations, args)

def svn_ra_get_file_revs(*args):
    """
    svn_ra_get_file_revs(svn_ra_session_t session, char path, svn_revnum_t start, 
        svn_revnum_t end, svn_ra_file_rev_handler_t handler, 
        void handler_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_file_revs, args)

def svn_ra_lock(*args):
    """
    svn_ra_lock(svn_ra_session_t session, apr_hash_t path_revs, char comment, 
        svn_boolean_t steal_lock, svn_ra_lock_callback_t lock_func, 
        void lock_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_lock, args)

def svn_ra_unlock(*args):
    """
    svn_ra_unlock(svn_ra_session_t session, apr_hash_t path_tokens, svn_boolean_t break_lock, 
        svn_ra_lock_callback_t lock_func, 
        void lock_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_unlock, args)

def svn_ra_get_lock(*args):
    """
    svn_ra_get_lock(svn_ra_session_t session, svn_lock_t lock, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_lock, args)

def svn_ra_get_locks(*args):
    """
    svn_ra_get_locks(svn_ra_session_t session, apr_hash_t locks, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_get_locks, args)

def svn_ra_replay(*args):
    """
    svn_ra_replay(svn_ra_session_t session, svn_revnum_t revision, svn_revnum_t low_water_mark, 
        svn_boolean_t send_deltas, 
        svn_delta_editor_t editor, void edit_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_replay, args)

def svn_ra_print_modules(*args):
    """svn_ra_print_modules(svn_stringbuf_t output, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_print_modules, args)

def svn_ra_print_ra_libraries(*args):
    """svn_ra_print_ra_libraries(svn_stringbuf_t descriptions, void ra_baton, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_print_ra_libraries, args)
class svn_ra_plugin_t:
    """Proxy of C svn_ra_plugin_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_ra_plugin_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_ra_plugin_t, name)
    def __repr__(self):
        return "<%s.%s; proxy of C svn_ra_plugin_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    __swig_setmethods__["name"] = _ra.svn_ra_plugin_t_name_set
    __swig_getmethods__["name"] = _ra.svn_ra_plugin_t_name_get
    __swig_setmethods__["description"] = _ra.svn_ra_plugin_t_description_set
    __swig_getmethods__["description"] = _ra.svn_ra_plugin_t_description_get
    __swig_setmethods__["open"] = _ra.svn_ra_plugin_t_open_set
    __swig_getmethods__["open"] = _ra.svn_ra_plugin_t_open_get
    __swig_setmethods__["get_latest_revnum"] = _ra.svn_ra_plugin_t_get_latest_revnum_set
    __swig_getmethods__["get_latest_revnum"] = _ra.svn_ra_plugin_t_get_latest_revnum_get
    __swig_setmethods__["get_dated_revision"] = _ra.svn_ra_plugin_t_get_dated_revision_set
    __swig_getmethods__["get_dated_revision"] = _ra.svn_ra_plugin_t_get_dated_revision_get
    __swig_setmethods__["change_rev_prop"] = _ra.svn_ra_plugin_t_change_rev_prop_set
    __swig_getmethods__["change_rev_prop"] = _ra.svn_ra_plugin_t_change_rev_prop_get
    __swig_setmethods__["rev_proplist"] = _ra.svn_ra_plugin_t_rev_proplist_set
    __swig_getmethods__["rev_proplist"] = _ra.svn_ra_plugin_t_rev_proplist_get
    __swig_setmethods__["rev_prop"] = _ra.svn_ra_plugin_t_rev_prop_set
    __swig_getmethods__["rev_prop"] = _ra.svn_ra_plugin_t_rev_prop_get
    __swig_setmethods__["get_commit_editor"] = _ra.svn_ra_plugin_t_get_commit_editor_set
    __swig_getmethods__["get_commit_editor"] = _ra.svn_ra_plugin_t_get_commit_editor_get
    __swig_setmethods__["get_file"] = _ra.svn_ra_plugin_t_get_file_set
    __swig_getmethods__["get_file"] = _ra.svn_ra_plugin_t_get_file_get
    __swig_setmethods__["get_dir"] = _ra.svn_ra_plugin_t_get_dir_set
    __swig_getmethods__["get_dir"] = _ra.svn_ra_plugin_t_get_dir_get
    __swig_setmethods__["do_update"] = _ra.svn_ra_plugin_t_do_update_set
    __swig_getmethods__["do_update"] = _ra.svn_ra_plugin_t_do_update_get
    __swig_setmethods__["do_switch"] = _ra.svn_ra_plugin_t_do_switch_set
    __swig_getmethods__["do_switch"] = _ra.svn_ra_plugin_t_do_switch_get
    __swig_setmethods__["do_status"] = _ra.svn_ra_plugin_t_do_status_set
    __swig_getmethods__["do_status"] = _ra.svn_ra_plugin_t_do_status_get
    __swig_setmethods__["do_diff"] = _ra.svn_ra_plugin_t_do_diff_set
    __swig_getmethods__["do_diff"] = _ra.svn_ra_plugin_t_do_diff_get
    __swig_setmethods__["get_log"] = _ra.svn_ra_plugin_t_get_log_set
    __swig_getmethods__["get_log"] = _ra.svn_ra_plugin_t_get_log_get
    __swig_setmethods__["check_path"] = _ra.svn_ra_plugin_t_check_path_set
    __swig_getmethods__["check_path"] = _ra.svn_ra_plugin_t_check_path_get
    __swig_setmethods__["get_uuid"] = _ra.svn_ra_plugin_t_get_uuid_set
    __swig_getmethods__["get_uuid"] = _ra.svn_ra_plugin_t_get_uuid_get
    __swig_setmethods__["get_repos_root"] = _ra.svn_ra_plugin_t_get_repos_root_set
    __swig_getmethods__["get_repos_root"] = _ra.svn_ra_plugin_t_get_repos_root_get
    __swig_setmethods__["get_locations"] = _ra.svn_ra_plugin_t_get_locations_set
    __swig_getmethods__["get_locations"] = _ra.svn_ra_plugin_t_get_locations_get
    __swig_setmethods__["get_file_revs"] = _ra.svn_ra_plugin_t_get_file_revs_set
    __swig_getmethods__["get_file_revs"] = _ra.svn_ra_plugin_t_get_file_revs_get
    __swig_setmethods__["get_version"] = _ra.svn_ra_plugin_t_get_version_set
    __swig_getmethods__["get_version"] = _ra.svn_ra_plugin_t_get_version_get
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_ra_plugin_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)

    def __init__(self, *args):
        """__init__(self) -> svn_ra_plugin_t"""
        _swig_setattr(self, svn_ra_plugin_t, 'this', apply(_ra.new_svn_ra_plugin_t, args))
        _swig_setattr(self, svn_ra_plugin_t, 'thisown', 1)
    def __del__(self, destroy=_ra.delete_svn_ra_plugin_t):
        """__del__(self)"""
        try:
            if self.thisown: destroy(self)
        except: pass


class svn_ra_plugin_tPtr(svn_ra_plugin_t):
    def __init__(self, this):
        _swig_setattr(self, svn_ra_plugin_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_ra_plugin_t, 'thisown', 0)
        _swig_setattr(self, svn_ra_plugin_t,self.__class__,svn_ra_plugin_t)
_ra.svn_ra_plugin_t_swigregister(svn_ra_plugin_tPtr)

SVN_RA_ABI_VERSION = _ra.SVN_RA_ABI_VERSION

def svn_ra_init_ra_libs(*args):
    """svn_ra_init_ra_libs(void ra_baton, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_init_ra_libs, args)

def svn_ra_get_ra_library(*args):
    """svn_ra_get_ra_library(svn_ra_plugin_t library, void ra_baton, char url, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_get_ra_library, args)
class svn_ra_session_t:
    """Proxy of C svn_ra_session_t struct"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svn_ra_session_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svn_ra_session_t, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C svn_ra_session_t instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    def set_parent_pool(self, parent_pool=None):
      """Create a new proxy object for svn_ra_session_t"""
      import libsvn.core, weakref
      self.__dict__["_parent_pool"] = \
        parent_pool or libsvn.core.application_pool;
      if self.__dict__["_parent_pool"]:
        self.__dict__["_is_valid"] = weakref.ref(
          self.__dict__["_parent_pool"]._is_valid)

    def assert_valid(self):
      """Assert that this object is using valid pool memory"""
      if "_is_valid" in self.__dict__:
        assert self.__dict__["_is_valid"](), "Variable has already been deleted"

    def __getattr__(self, name):
      """Get an attribute from this object"""
      self.assert_valid()
      value = _swig_getattr(self, self.__class__, name)
      try:
        old_dict = self.__dict__["_member_dicts"][name]
        value.__dict__["_parent_pool"] = old_dict.get("_parent_pool")
        value.__dict__["_member_dicts"] = old_dict.get("_member_dicts")
        value.__dict__["_is_valid"] = old_dict.get("_is_valid")
        value.assert_valid()
      except KeyError:
        pass
      return value

    def __setattr__(self, name, value):
      """Set an attribute on this object"""
      self.assert_valid()
      try:
        self.__dict__.setdefault("_member_dicts",{})[name] = value.__dict__
      except AttributeError:
        pass
      return _swig_setattr(self, self.__class__, name, value)


class svn_ra_session_tPtr(svn_ra_session_t):
    def __init__(self, this):
        _swig_setattr(self, svn_ra_session_t, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, svn_ra_session_t, 'thisown', 0)
        _swig_setattr(self, svn_ra_session_t,self.__class__,svn_ra_session_t)
_ra.svn_ra_session_t_swigregister(svn_ra_session_tPtr)


def svn_ra_reporter2_invoke_set_path(*args):
    """
    svn_ra_reporter2_invoke_set_path(svn_ra_reporter2_t _obj, void report_baton, char path, 
        svn_revnum_t revision, svn_boolean_t start_empty, 
        char lock_token, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_reporter2_invoke_set_path, args)

def svn_ra_reporter2_invoke_delete_path(*args):
    """
    svn_ra_reporter2_invoke_delete_path(svn_ra_reporter2_t _obj, void report_baton, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_reporter2_invoke_delete_path, args)

def svn_ra_reporter2_invoke_link_path(*args):
    """
    svn_ra_reporter2_invoke_link_path(svn_ra_reporter2_t _obj, void report_baton, char path, 
        char url, svn_revnum_t revision, svn_boolean_t start_empty, 
        char lock_token, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_reporter2_invoke_link_path, args)

def svn_ra_reporter2_invoke_finish_report(*args):
    """svn_ra_reporter2_invoke_finish_report(svn_ra_reporter2_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_reporter2_invoke_finish_report, args)

def svn_ra_reporter2_invoke_abort_report(*args):
    """svn_ra_reporter2_invoke_abort_report(svn_ra_reporter2_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_reporter2_invoke_abort_report, args)

def svn_ra_reporter_invoke_set_path(*args):
    """
    svn_ra_reporter_invoke_set_path(svn_ra_reporter_t _obj, void report_baton, char path, 
        svn_revnum_t revision, svn_boolean_t start_empty, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_reporter_invoke_set_path, args)

def svn_ra_reporter_invoke_delete_path(*args):
    """
    svn_ra_reporter_invoke_delete_path(svn_ra_reporter_t _obj, void report_baton, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_reporter_invoke_delete_path, args)

def svn_ra_reporter_invoke_link_path(*args):
    """
    svn_ra_reporter_invoke_link_path(svn_ra_reporter_t _obj, void report_baton, char path, 
        char url, svn_revnum_t revision, svn_boolean_t start_empty, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_reporter_invoke_link_path, args)

def svn_ra_reporter_invoke_finish_report(*args):
    """svn_ra_reporter_invoke_finish_report(svn_ra_reporter_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_reporter_invoke_finish_report, args)

def svn_ra_reporter_invoke_abort_report(*args):
    """svn_ra_reporter_invoke_abort_report(svn_ra_reporter_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t"""
    return apply(_ra.svn_ra_reporter_invoke_abort_report, args)

def svn_ra_callbacks2_invoke_open_tmp_file(*args):
    """
    svn_ra_callbacks2_invoke_open_tmp_file(svn_ra_callbacks2_t _obj, apr_file_t fp, void callback_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_callbacks2_invoke_open_tmp_file, args)

def svn_ra_callbacks_invoke_open_tmp_file(*args):
    """
    svn_ra_callbacks_invoke_open_tmp_file(svn_ra_callbacks_t _obj, apr_file_t fp, void callback_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_callbacks_invoke_open_tmp_file, args)

def svn_ra_plugin_invoke_open(*args):
    """
    svn_ra_plugin_invoke_open(svn_ra_plugin_t _obj, void session_baton, char repos_URL, 
        svn_ra_callbacks_t callbacks, void callback_baton, 
        apr_hash_t config, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_open, args)

def svn_ra_plugin_invoke_get_latest_revnum(*args):
    """
    svn_ra_plugin_invoke_get_latest_revnum(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t latest_revnum, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_latest_revnum, args)

def svn_ra_plugin_invoke_get_dated_revision(*args):
    """
    svn_ra_plugin_invoke_get_dated_revision(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t revision, 
        apr_time_t tm, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_dated_revision, args)

def svn_ra_plugin_invoke_change_rev_prop(*args):
    """
    svn_ra_plugin_invoke_change_rev_prop(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t rev, 
        char name, svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_change_rev_prop, args)

def svn_ra_plugin_invoke_rev_proplist(*args):
    """
    svn_ra_plugin_invoke_rev_proplist(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t rev, 
        apr_hash_t props, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_rev_proplist, args)

def svn_ra_plugin_invoke_rev_prop(*args):
    """
    svn_ra_plugin_invoke_rev_prop(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t rev, 
        char name, svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_rev_prop, args)

def svn_ra_plugin_invoke_get_commit_editor(*args):
    """
    svn_ra_plugin_invoke_get_commit_editor(svn_ra_plugin_t _obj, void session_baton, svn_delta_editor_t editor, 
        void edit_baton, char log_msg, 
        svn_commit_callback_t callback, void callback_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_commit_editor, args)

def svn_ra_plugin_invoke_get_file(*args):
    """
    svn_ra_plugin_invoke_get_file(svn_ra_plugin_t _obj, void session_baton, char path, 
        svn_revnum_t revision, svn_stream_t stream, 
        svn_revnum_t fetched_rev, apr_hash_t props, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_file, args)

def svn_ra_plugin_invoke_get_dir(*args):
    """
    svn_ra_plugin_invoke_get_dir(svn_ra_plugin_t _obj, void session_baton, char path, 
        svn_revnum_t revision, apr_hash_t dirents, 
        svn_revnum_t fetched_rev, apr_hash_t props, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_dir, args)

def svn_ra_plugin_invoke_do_update(*args):
    """
    svn_ra_plugin_invoke_do_update(svn_ra_plugin_t _obj, void session_baton, svn_ra_reporter_t reporter, 
        void report_baton, svn_revnum_t revision_to_update_to, 
        char update_target, 
        svn_boolean_t recurse, svn_delta_editor_t update_editor, 
        void update_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_do_update, args)

def svn_ra_plugin_invoke_do_switch(*args):
    """
    svn_ra_plugin_invoke_do_switch(svn_ra_plugin_t _obj, void session_baton, svn_ra_reporter_t reporter, 
        void report_baton, svn_revnum_t revision_to_switch_to, 
        char switch_target, 
        svn_boolean_t recurse, char switch_url, svn_delta_editor_t switch_editor, 
        void switch_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_do_switch, args)

def svn_ra_plugin_invoke_do_status(*args):
    """
    svn_ra_plugin_invoke_do_status(svn_ra_plugin_t _obj, void session_baton, svn_ra_reporter_t reporter, 
        void report_baton, char status_target, 
        svn_revnum_t revision, svn_boolean_t recurse, 
        svn_delta_editor_t status_editor, 
        void status_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_do_status, args)

def svn_ra_plugin_invoke_do_diff(*args):
    """
    svn_ra_plugin_invoke_do_diff(svn_ra_plugin_t _obj, void session_baton, svn_ra_reporter_t reporter, 
        void report_baton, svn_revnum_t revision, 
        char diff_target, svn_boolean_t recurse, 
        svn_boolean_t ignore_ancestry, char versus_url, 
        svn_delta_editor_t diff_editor, 
        void diff_baton, apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_do_diff, args)

def svn_ra_plugin_invoke_get_log(*args):
    """
    svn_ra_plugin_invoke_get_log(svn_ra_plugin_t _obj, void session_baton, apr_array_header_t paths, 
        svn_revnum_t start, svn_revnum_t end, 
        svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, svn_log_message_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_log, args)

def svn_ra_plugin_invoke_check_path(*args):
    """
    svn_ra_plugin_invoke_check_path(svn_ra_plugin_t _obj, void session_baton, char path, 
        svn_revnum_t revision, svn_node_kind_t kind, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_check_path, args)

def svn_ra_plugin_invoke_get_uuid(*args):
    """
    svn_ra_plugin_invoke_get_uuid(svn_ra_plugin_t _obj, void session_baton, char uuid, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_uuid, args)

def svn_ra_plugin_invoke_get_repos_root(*args):
    """
    svn_ra_plugin_invoke_get_repos_root(svn_ra_plugin_t _obj, void session_baton, char url, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_repos_root, args)

def svn_ra_plugin_invoke_get_locations(*args):
    """
    svn_ra_plugin_invoke_get_locations(svn_ra_plugin_t _obj, void session_baton, apr_hash_t locations, 
        char path, svn_revnum_t peg_revision, 
        apr_array_header_t location_revisions, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_locations, args)

def svn_ra_plugin_invoke_get_file_revs(*args):
    """
    svn_ra_plugin_invoke_get_file_revs(svn_ra_plugin_t _obj, void session_baton, char path, 
        svn_revnum_t start, svn_revnum_t end, svn_ra_file_rev_handler_t handler, 
        void handler_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    return apply(_ra.svn_ra_plugin_invoke_get_file_revs, args)

