import React from 'react'
import { sidebarAdmin, sidebarLinks } from '../assets/sidebarLinks'

const Sidebar = ({handleShow}) => {

    
  return (
    <div className={`${handleShow ? 'fixed': 'hidden'}`}  >
        <div className='relative  bg-slate-100 w-fit md:w-[200px] px-3 h-screen border-r border-gray-300 p-4 text-sm font-bold  text-md '>
            <div className=' bg-blue-500 w-[40px] h-[40px] text-center text-white rounded-full'>
                <p className=' font-Lobster font-bold text-3xl'>A</p>
            </div>
            
            <h3 className=' font-bold text-xl mb-5 '>AgileNest</h3>
            <p className=' border-b border-gray-300 my-4'></p>
        
        <div className=''>
            {sidebarLinks.map((link, index) => (
                <div className=' flex '>
                   
                    <p key={index} className=' mb-4 flex items-center gap-3'>{link.icon}{link.name}</p>
                </div>
            ) )}
        </div>


        <div className=' absolute bottom-4 capitalize'>
            <h3 className=' font-bold text-lg'>ADMINISTRATION</h3>
            {sidebarAdmin.map((link) => (
                <p className=' flex gap-3 my-4'>{link.icon} {link.name}</p>
            ))}
          
        </div>
        </div>
    </div>
  )
}

export default Sidebar