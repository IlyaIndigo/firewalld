#
# Copyright (C) 2011 Red Hat, Inc.
# Authors:
# Thomas Woerner <twoerner@redhat.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

DBUS_INTERFACE_VERSION = 1
DBUS_INTERFACE_REVISION = 0

DBUS_INTERFACE = "org.fedoraproject.FirewallD%d" % DBUS_INTERFACE_VERSION
DBUS_INTERFACE_ZONE = DBUS_INTERFACE+".zone"
DBUS_INTERFACE_DIRECT = DBUS_INTERFACE+".direct"
DBUS_INTERFACE_CONFIG = DBUS_INTERFACE+".config"

DBUS_PATH = "/org/fedoraproject/FirewallD%d" % DBUS_INTERFACE_VERSION
DBUS_PATH_CONFIG = DBUS_PATH+"/config"
DBUS_PATH_CONFIG_ICMPTYPE = DBUS_PATH+"/config/icmptype"
DBUS_PATH_CONFIG_SERVICE = DBUS_PATH+"/config/service"
DBUS_PATH_CONFIG_ZONE = DBUS_PATH+"/config/zone"

_PK_ACTION = "org.fedoraproject.FirewallD%d" % DBUS_INTERFACE_VERSION
PK_ACTION_CONFIG = _PK_ACTION+".config"
PK_ACTION_DIRECT = _PK_ACTION+".direct"
PK_ACTION_INFO = _PK_ACTION+".info"
#PK_ACTION_MODIFY = _PK_ACTION+".modify"
