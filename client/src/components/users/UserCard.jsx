import React from 'react'

const UserCard = ({ user }) => {
  return (
    <li>{ user.username }</li>
  )
}

export default UserCard