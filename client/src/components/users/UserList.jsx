import React from 'react'
import UserCard from './UserCard'

const UserList = ({ users }) => {
  const userCards = users.map(user => <UserCard key={ user.id } user={ user } />)
  return (
    <ul>
      { userCards }
    </ul>
  )
}

export default UserList