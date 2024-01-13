import { RiHome4Line } from "react-icons/ri";
import { MdOutlineSpaceDashboard } from "react-icons/md";
import { GoProjectSymlink , GoSignOut} from "react-icons/go";
import { IoListOutline } from "react-icons/io5";
import { FaRegUser, FaRegStar } from "react-icons/fa";
import { HiOutlineDocumentReport } from "react-icons/hi";
import { RiTeamLine } from "react-icons/ri";
import { CiHeadphones } from "react-icons/ci";




export const sidebarLinks = [
    {
        name: 'overview',
        url: '/overview',
        icon: <RiHome4Line />
    },

    {
        name: 'dashbaord',
        url: '/dashboard',
        icon: <MdOutlineSpaceDashboard />
    },

    {
        name: 'projects',
        url: '/projects',
        icon: <GoProjectSymlink />
    },

    {
        name: 'tasks',
        url: '/tasks',
        icon: <IoListOutline />
    },


    {
        name: 'employees',
        url: '/employees',
        icon: <FaRegUser />
    },


    {
        name: 'reports',
        url: '/reports',
        icon: <HiOutlineDocumentReport />
    },

    {
        name: 'collaboration',
        url: '/collaboration',
        icon: <RiTeamLine />
    },

  
]


export const sidebarAdmin = [
    {
        name: 'integrations',
        url: '/integrations',
        icon: <FaRegStar />

    },

    {
        name: 'support',
        url: '/support',
        icon: <CiHeadphones />
    },

    {
        name: 'sign out',
        url: '/signout',
        icon: <GoSignOut />
    }
]