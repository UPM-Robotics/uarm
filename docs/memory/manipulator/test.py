#                             src
#                  Copyright (C) 2019 - Javinator9889
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#                   (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#               GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
from numpy import ndindex
from time import time

from . import DHTable
from . import Symbol
from . import pi
from . import Manipulator
from . import cos
from . import to_latrix
from sympy import latex
from sympy import simplify
from sympy import symbols


def main():
    table = DHTable()
    t1, t2, t3 = symbols("theta_1 theta_2 theta_3")
    table.add(theta=t1, d=106.1, a=13.2, alpha=(pi / 2)) \
        .add(theta=t2, d=0, a=142, alpha=pi) \
        .add(theta=t3, d=0, a=158.9, alpha=0)
    # \
    # .add(theta=((pi / 2) - (Symbol("theta_2") + Symbol("theta_3"))), d=0, a=44.5,
    #      alpha=0)
    # print(table.get())
    print(table)
    # table2 = DHTable()
    # table2.add(theta=Symbol("theta_1"), d=Symbol("a_1"),
    #            a=Symbol("d_1"), alpha=(pi / 2), check_attrs=False) \
    #     .add(theta=Symbol("theta_2"), d=0, a=Symbol("a_2"), alpha=pi, check_attrs=False) \
    #     .add(theta=Symbol("theta_3"), d=0, a=Symbol("a_3"), alpha=0, check_attrs=False)
    # table2.Tx = Symbol("T_X")
    # table2.Tz = -Symbol("T_Z")
    # # \
    # # .add(theta=((pi / 2) - (Symbol("theta_2") + Symbol("theta_3"))), d=0,
    # #      a=Symbol("a_4"), alpha=0, check_attrs=False)
    # print(table2)
    # calc_times = set()
    # sub_times = set()
    # for i in range(10):
    #     stt = time()
    #     m = Manipulator(params=table)
    #     stp = time()
    #     print("Elapsed time for calculating matrices: {:.3f}s".format(stp - stt))
    #     calc_times.add(stp - stt)
    #     # print(m["A04"])
    #     stt = time()
    #     rs = m.point(symbols={Symbol("theta_1"): 0,
    #                           Symbol("theta_2"): 0,
    #                           Symbol("theta_3"): pi,
    #                           Symbol("theta_4"): pi})
    #     stp = time()
    #     print("Elapsed time for applying matrix changes: {:.3f}s".format(stp - stt))
    #     sub_times.add(stp - stt)
    # print("Average calc. time: {:.3f}s".format(sum(calc_times) / 10))
    # print("Average sub. time: {:.3f}s".format(sum(sub_times) / 10))
    m = Manipulator(params=table)
    c1 = m.point({t1: 0, t2: 0, t3: 0})
    c2 = m.point({t1: 0, t2: pi / 2, t3: 0})
    c3 = m.point({t1: -pi / 2, t2: 0, t3: 0})
    c4 = m.point({t1: pi, t2: pi / 2, t3: pi / 4})
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    # m2 = Manipulator(params=table2)
    # # print(m.direct_kinematics["A04"])
    # print(m2.direct_kinematics["A01"])
    # print(m2.direct_kinematics["A12"])
    # print(m2.direct_kinematics["A23"])
    # print(m2.direct_kinematics["A02"])
    # print(m2.direct_kinematics["A03"])
    # print(m2.to_latrix("p", "A01"))
    # print(m2.to_latrix("p", "A12"))
    # print(m2.to_latrix("p", "A23"))
    # print(m2.to_latrix("p", "A02"))
    # print(m2.to_latrix("p", "A03"))
    # print(f"Xe: {m2.inverse_kinematics.Xe}")
    # # print(m.inverse_kinematics.Ye)
    # print(f"Ze: {m2.inverse_kinematics.Ze}")
    # Xe1 = m2.inverse_kinematics.Xe / cos(Symbol("theta_1"))
    # Ze = m2.inverse_kinematics.Ze
    # Xe12 = (Xe1 ** 2).expand()
    # Ze2 = (Ze ** 2).expand()
    # print(f"Xe': {Xe1}")
    # print(f"Xe'2: {Xe12}")
    # print(f"Ze2: {Ze2}")
    # sq_add = (Xe12 + Ze2).expand().simplify()
    # print(f"Add: {sq_add}")
    # print(f"Xe'2: {latex(Xe12)}")
    # print(f"Ze2: {latex(Ze2)}")
    # print(f"Add: {latex(sq_add)}")
    #
    # m2.set_phi('x', Symbol("theta_2") - Symbol("theta_3"))
    # m2.set_phi('y', 0)
    # m2.set_phi('z', Symbol("theta_1"))
    # j = m2.jacobian(symbols=[Symbol("theta_1"), Symbol("theta_2"), Symbol("theta_3")])
    # j1 = m2.inverse_kinematics.upper_jacobian
    # j2 = m2.inverse_kinematics.lower_jacobian
    # print(j1)
    # print(j2)
    # print(j)
    # print(to_latrix('p', j))
    # print(to_latrix('p', j1))
    # print(m2.inverse_kinematics.det)
    # print("LaTeX")
    # print(latex(m2.inverse_kinematics.det))
    # print("Inverse Jacobian")
    # print(m2.inverse_kinematics.i_jacobian)
    # print(to_latrix('p', m2.inverse_kinematics.i_jacobian))
    # from time import time
    # print("J+")
    # st = time()
    # pinv1 = j1.pinv()
    # end = time()
    # print("Elapsed time: {:.3f}".format(end - st))
    # print(pinv1)
    # st = time()
    # pinv1 = simplify(pinv1)
    # end = time()
    # print("Elapsed time: {:.3f}".format(end - st))
    # print(pinv1)
    # print(latex(pinv1))
    # j_1 = m2.inverse_kinematics.upper_jacobian * m2.inverse_kinematics.upper_jacobian.T
    # print(j_1)
    # j_1 = simplify(j_1)
    # print(j_1)
    # ij_1 = j_1 ** -1
    # print(ij_1)
    # ij_1 = simplify(ij_1)
    # print(ij_1)
    # jp = m2.inverse_kinematics.upper_jacobian * ij_1
    # print(jp)
    # jp = simplify(jp)
    # print(jp)
    # m2.inverse_kinematics.pseudo_inverse(optimize=False)
    # print(m2.inverse_kinematics.pseudo_i_jacobian)
    # print(to_latrix('p', m2.inverse_kinematics.pseudo_i_jacobian))
    # m2.inverse_kinematics.pseudo_inverse(optimize=True)
    # print(m2.inverse_kinematics.pseudo_i_jacobian)
    # print(to_latrix('p', m2.inverse_kinematics.pseudo_i_jacobian))
    # print(m.inverse_kinematics.sq_points_add)
    # print(((m.inverse_kinematics.Xe ** 2) + (m.inverse_kinematics.Ye ** 2)).simplify())
    # for i, j in ndindex((m.params.max, m.params.max)):
    # print(m.to_latrix("p", f"A{i}{j}"))
    # print(m.to_latrix("p", "A01"))
    # print(m.to_latrix("p", "A02"))
    # print(m.to_latrix("p", "A03"))
    # print(m.to_latrix("p", "A04"))
    # print(m.to_latrix("p", "A12"))
    # print(m.to_latrix("p", "A23"))
    # print(m.to_latrix("p", "A34"))
    # m.set_phi(Symbol("theta_2") + Symbol("theta_3") + Symbol("theta_4"))
    # print(m.inverse_kinematics.sq_points_add)
    # print("Solving equations...")
    # solution = solve()
    # solution.subs()
    # print(solution)
    # print(latex(solution))
    # sol = m.solve((1, 1, 1), pi / 2)
    # print(sol)
    # print(rs)
    # print(m.to_latrix('p', rs))
    # print(m.to_latrix('p', "A04"))


def solve():
    from sympy.solvers import nonlinsolve
    from sympy import symbols
    from sympy import sin, cos, pi

    t2, t3, t4 = symbols("theta_2 theta_3 theta_4")
    a1, a2, a3, a4, d1, L, Ze = symbols("a_1 a_2 a_3 a_4 d_1 L Z_e")
    pi2 = pi / 2
    # expr1 = a2 * cos(t2) + a3 * cos(t2 + t3) + a4 * cos(t2 + t3 + (pi2 - (t2 + t3))) + \
    #         d1 - L
    # print(expr1.simplify())
    # expr2 = (a2 * sin(t2) + a1) - (a4 * sin(t2 + t3 + (pi2 - (t2 + t3))) +
    #                                a3 * sin(t2 + t3)) - Ze
    # print(expr2.simplify())
    # expr1 = expr1.subs({a1: 10, a2: 10, a3: 10, d1: 0, L: 30})
    # expr2 = expr2.subs({a1: 10, a2: 10, a3: 10, d1: 0, Ze: 30})
    expr1 = 10 * cos(t2) + 10 * cos(t2 + t3) - 3
    expr2 = - 1 + 10 * sin(t2) - 10 * sin(t2 + t3)
    system = [expr1, expr2]
    symbs = [t2, t3]
    return nonlinsolve(system, symbs)