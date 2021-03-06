import React, { useEffect } from 'react';
import { connect } from 'react-redux';

const WrapperComponent = WrappedComponent => {
	const AuthComponent = props => {
		const { authenticated, history, location } = props;

		useEffect(() => {
			const userRedirect = () => {
				const path = location.pathname;
				if (localStorage.getItem('token') || authenticated) history.push(path);
				else history.push('/');
			};
			userRedirect();
		}, [authenticated, history, location.pathname]);

		return <WrappedComponent {...props} />;
	};
	const mapStateToProps = ({ user: { authenticated } }) => ({
		authenticated,
	});
	return connect(mapStateToProps)(AuthComponent);
};
export default WrapperComponent;
