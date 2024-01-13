import React from 'react'
import { IoIosNotificationsOutline } from "react-icons/io";
import { HiBars3 } from "react-icons/hi2";


const Navbar = ({handleShow}) => {

    

    
  return (
    <div className=' bg-gray-100 '>
        <div className=' flex items-center justify-between py-4 px-10'>
            <HiBars3 className='' size={30} />
            <div className=' flex items-center gap-5'>
                <span className='relative '>
                    <IoIosNotificationsOutline onClick={handleShow} className='' size={20} />
                    <div className=' bg-red-500 w-4 h-4 flex items-center justify-center rounded-full text-center text-xs text-white absolute top-2 right-2'>
                        <p className=''>8</p>
                    </div>
                    
                </span>
                
                <div className=' flex gap-2 items-center '>
                    <div className=' bg-gray-400 w-10 h-10 rounded-full flex items-center justify-center'>
                        <img src='/bs.png' alt='avatar'   />
                    </div>
                   
                    <p className=' text-sm font-bold'>Joshua</p>
                </div>
            </div>
        </div>
    </div>
  )
}

export default Navbar