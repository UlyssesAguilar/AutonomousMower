/*
 * A-Frame component that rerenders the image in an `<a-sky>` whenever a
 * `rerender_sky` event is occurs. `rerender_sky` events are triggered
 * whenever a new frame is received, but can be setup to be triggered
 * on an interval to achieve a framerate independent of the actual video
 * framerate.
 */
AFRAME.registerComponent('updater', {
    init: function() {
        console.log("TESTING")
        //var data = this.data;
        //var el = this.el;
    }

    tick: function() {
        console.log("TESTING")
        //el.object3DMap.mesh.material.map.image.src = this.el;
    }
});
