##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RRmpi(RPackage):
    """An interface (wrapper) to MPI APIs. It also provides interactive R
       manager and worker environment."""

    homepage = "http://www.stats.uwo.ca/faculty/yu/Rmpi"
    url      = "https://cran.r-project.org/src/contrib/Rmpi_0.6-6.tar.gz"

    version('0.6-6', '59ae8ce62ff0ff99342d53942c745779')

    depends_on('mpi')
    depends_on('r@2.15.1:')

    # The following MPI types are not supported
    conflicts('^intel-mpi')
    conflicts('^intel-parallel-studio')
    conflicts('^mvapich2')
    conflicts('^spectrum-mpi')

    def configure_args(self, spec, prefix):
        mpi_name = spec['mpi'].name

        # The type of MPI. Supported values are:
        # OPENMPI, LAM, MPICH, MPICH2, or CRAY
        if mpi_name == 'openmpi':
            Rmpi_type = 'OPENMPI'
        elif mpi_name == 'mpich':
            Rmpi_type = 'MPICH2'
        else:
            raise InstallError('Unsupported MPI type')

        return [
            '--with-Rmpi-type={0}'.format(Rmpi_type),
            '--with-mpi={0}'.format(spec['mpi'].prefix),
        ]
